(function () {
  'use strict';

  const SITE_URL = 'https://thebizplans.com/';
  const ORGANIZATION_ID = `${SITE_URL}#organization`;
  const path = window.location.pathname;
  const fileName = path.split('/').pop() || 'index.html';
  const isHome = path === '/' || fileName === 'index.html';
  const pageUrl = isHome ? SITE_URL : `${SITE_URL}${fileName}`;
  const title = document.title.replace(/\s*\|\s*The Biz Plans\s*$/, '').trim();
  const description = document.querySelector('meta[name="description"]')?.content || '';
  const ogType = document.querySelector('meta[property="og:type"]')?.content;
  const ogImage = document.querySelector('meta[property="og:image"]')?.content;

  const existingTypes = new Set();
  document.querySelectorAll('script[type="application/ld+json"]').forEach((script) => {
    try {
      const visit = (value) => {
        if (!value || typeof value !== 'object') return;
        const types = Array.isArray(value['@type']) ? value['@type'] : [value['@type']];
        types.filter(Boolean).forEach((type) => existingTypes.add(type));
        Object.values(value).forEach(visit);
      };
      visit(JSON.parse(script.textContent));
    } catch (error) {
      console.warn('Unable to read existing structured data.', error);
    }
  });

  const graph = [];
  const addUnlessPresent = (node) => {
    const types = Array.isArray(node['@type']) ? node['@type'] : [node['@type']];
    if (!types.some((type) => existingTypes.has(type))) graph.push(node);
  };

  // This canonical node gives every generated reference a resolvable @id, even
  // on legacy pages whose inline Organization markup does not define one.
  graph.push({
    '@type': 'Organization',
    '@id': ORGANIZATION_ID,
    name: 'The Biz Plans',
    url: SITE_URL,
    logo: `${SITE_URL}img/bizplanlogo.png`,
    email: 'info@thebizplans.com',
    telephone: '+1-647-896-8362',
    sameAs: [
      'https://www.instagram.com/thebizplans/',
      'https://www.facebook.com/people/The-biz-plans/61550125095965/',
      'https://www.linkedin.com/company/thebizplans'
    ]
  });

  if (isHome) {
    addUnlessPresent({
      '@type': 'LocalBusiness',
      '@id': `${SITE_URL}#localbusiness`,
      name: 'The Biz Plans',
      url: SITE_URL,
      image: `${SITE_URL}img/hero-bizplans.png`,
      telephone: '+1-647-896-8362',
      address: {
        '@type': 'PostalAddress',
        streetAddress: '51 Burnhamill Pl',
        addressLocality: 'Toronto',
        addressRegion: 'ON',
        postalCode: 'M9C 3S3',
        addressCountry: 'CA'
      },
      parentOrganization: { '@id': ORGANIZATION_ID }
    });
    addUnlessPresent({
      '@type': 'WebSite',
      '@id': `${SITE_URL}#website`,
      url: SITE_URL,
      name: 'The Biz Plans',
      publisher: { '@id': ORGANIZATION_ID },
      potentialAction: {
        '@type': 'SearchAction',
        target: `${SITE_URL}search.html?q={search_term_string}`,
        'query-input': 'required name=search_term_string'
      }
    });
  } else {
    addUnlessPresent({
      '@type': 'BreadcrumbList',
      '@id': `${pageUrl}#breadcrumb`,
      itemListElement: [
        { '@type': 'ListItem', position: 1, name: 'Home', item: SITE_URL },
        { '@type': 'ListItem', position: 2, name: title, item: pageUrl }
      ]
    });

    const isArticle = fileName.startsWith('blog-') || fileName.startsWith('chapter-') || ogType === 'article';
    const isService = /business-plan|services|financial-modeling|marketing-growth-strategy|pricing/.test(fileName) ||
      /business plans?|business planning/i.test(title);

    if (isArticle) {
      addUnlessPresent({
        '@type': 'Article',
        '@id': `${pageUrl}#article`,
        headline: title,
        description,
        mainEntityOfPage: pageUrl,
        ...(ogImage ? { image: ogImage } : {}),
        author: { '@type': 'Person', name: 'Atul Jagga' },
        publisher: { '@id': ORGANIZATION_ID },
        inLanguage: 'en-CA'
      });
    } else if (isService) {
      addUnlessPresent({
        '@type': 'Service',
        '@id': `${pageUrl}#service`,
        name: title,
        description,
        url: pageUrl,
        provider: { '@id': ORGANIZATION_ID },
        areaServed: { '@type': 'Country', name: 'Canada' }
      });
    } else {
      addUnlessPresent({
        '@type': 'WebPage',
        '@id': `${pageUrl}#webpage`,
        url: pageUrl,
        name: title,
        description,
        isPartOf: { '@id': `${SITE_URL}#website` },
        about: { '@id': ORGANIZATION_ID },
        inLanguage: 'en-CA'
      });
    }
  }

  if (graph.length) {
    const schema = document.createElement('script');
    schema.type = 'application/ld+json';
    schema.textContent = JSON.stringify({ '@context': 'https://schema.org', '@graph': graph });
    document.head.appendChild(schema);
  }
})();
