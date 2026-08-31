(function () {
  'use strict';

  const SITE_URL = 'https://thebizplans.com/';
  const ORGANIZATION_ID = `${SITE_URL}#organization`;
  const PERSON_ID = `${SITE_URL}#atul-jagga`;
  const path = window.location.pathname;
  const fileName = path.split('/').pop() || 'index.html';
  const isHome = path === '/' || fileName === 'index.html';
  const pageUrl = isHome ? SITE_URL : `${SITE_URL}${fileName}`;
  const pageName = (
    document.querySelector('h1')?.textContent ||
    document.querySelector('meta[property="og:title"]')?.content ||
    document.title.split('|')[0]
  ).replace(/\s+/g, ' ').trim();
  const description = document.querySelector('meta[name="description"]')?.content || '';
  const ogType = document.querySelector('meta[property="og:type"]')?.content;
  const ogImage = document.querySelector('meta[property="og:image"]')?.content;

  const crumb = (name, file) => ({ name, url: file ? `${SITE_URL}${file}` : SITE_URL });
  const industryNames = [
    'beauty-salon', 'cannabis', 'construction', 'daycare', 'grocery', 'hvac',
    'logistics', 'manufacturing', 'nail-salon', 'pharmacy', 'plumbing', 'trucking'
  ];
  const industry = industryNames.find((name) => fileName.startsWith(`${name}-`));

  function getBreadcrumbs() {
    const items = [crumb('Home')];
    const add = (name, file) => items.push(crumb(name, file));
    const financingPages = /^(bank-loan-business-plans|black-entrepreneurship|business-development-bank-of-canada|canada-small-business-financing-program|canadian-agricultural-loans-act|canadian-bank-loan-business-plan-guide|cibc|desjardins|export-development-canada|farm-credit-canada|futurpreneur|how-banks-evaluate-business-plans|indigenous-aboriginal-entrepreneurship|national-bank-of-canada|private-lender-alternative-financing|royal-bank-of-canada|scotiabank|small-business-financing-canada|td-canada-trust|vancity-business-plan|women-entrepreneurship-loan-fund)\.html$/;
    const immigrationPages = /^(aaip-entrepreneur-business-plan|bcpnp-business-plan|ict-business-plan|immigration-business-plans|indigenous-business-plan|innovation-business-plan|lmia-owner-operator-business-plan|mpnp-business-plan|nbpnp-business-plan|nsnp-business-plan|oinp-business-plan|self-employed-business-plan|sinp-business-plan|startup-visa-business-plan)\.html$/;
    const servicePages = /^(business-plan-review|financial-modeling|investor-business-plan|marketing-growth-strategy|services|strategic-business-plan)\.html$/;
    const learningPages = /^(authoritative-resources|blog-|books|business-plan-comparisons|business-plan-cost-timeline-checklist|business-plan-essentials|business-plan-glossary|chapter-|faqs|financial-due-diligence-essentials)/;

    if (industry || /^(brewery|fintech|food-franchise|marine|medical-services|mobile-app|recruiting|telecom)-business-plans\.html$/.test(fileName)) {
      add('Industries', 'industry-business-plans.html');
      if (industry && fileName !== `${industry}-business-plans.html`) {
        const label = industry.replace(/(^|-)(\w)/g, (_, separator, letter) => `${separator ? ' ' : ''}${letter.toUpperCase()}`);
        add(`${label} Business Plans`, `${industry}-business-plans.html`);
      }
    } else if (fileName === 'industry-business-plans.html') {
      // Home is the only ancestor of this section landing page.
    } else if (financingPages.test(fileName)) {
      if (fileName !== 'bank-loan-business-plans.html') add('Financing Resource Centre', 'bank-loan-business-plans.html');
    } else if (immigrationPages.test(fileName)) {
      if (fileName !== 'immigration-business-plans.html') add('Immigration Business Plans', 'immigration-business-plans.html');
    } else if (servicePages.test(fileName)) {
      if (fileName !== 'services.html') add('Services', 'services.html');
    } else if (learningPages.test(fileName)) {
      if (fileName !== 'blog-learning-hub.html') add('Learning Centre', 'blog-learning-hub.html');
      if (fileName.startsWith('chapter-')) add('Business Plan Essentials', 'business-plan-essentials.html');
    } else if (/^(toronto|vancouver)-business-plan-writers\.html$/.test(fileName)) {
      add('About', 'about-business-plan.html');
    }

    items.push({ name: pageName, url: pageUrl, current: true });
    return items;
  }

  const breadcrumbs = isHome ? [] : getBreadcrumbs();

  // Remove legacy breadcrumbs so there is one visible trail and one structured
  // trail, both generated from the hierarchy above.
  if (!isHome) {
    document.querySelectorAll('nav[aria-label="Breadcrumb"], nav[aria-label="breadcrumb"], .cluster-breadcrumb').forEach((node) => node.remove());
    document.querySelectorAll('script[type="application/ld+json"]').forEach((script) => {
      try {
        const data = JSON.parse(script.textContent);
        if (Array.isArray(data['@graph'])) {
          data['@graph'] = data['@graph'].filter((node) => node['@type'] !== 'BreadcrumbList');
          script.textContent = JSON.stringify(data);
        } else if (data['@type'] === 'BreadcrumbList') {
          script.remove();
        }
      } catch (error) {
        console.warn('Unable to read existing structured data.', error);
      }
    });

    const nav = document.createElement('nav');
    nav.className = 'site-breadcrumb';
    nav.setAttribute('aria-label', 'Breadcrumb');
    const list = document.createElement('ol');
    breadcrumbs.forEach((item) => {
      const listItem = document.createElement('li');
      if (item.current) {
        listItem.textContent = item.name;
        listItem.setAttribute('aria-current', 'page');
      } else {
        const link = document.createElement('a');
        link.href = item.url;
        link.textContent = item.name;
        listItem.appendChild(link);
      }
      list.appendChild(listItem);
    });
    nav.appendChild(list);
    const menu = document.querySelector('.sticky-top');
    if (menu) menu.insertAdjacentElement('afterend', nav);
    else document.body.insertAdjacentElement('afterbegin', nav);
  }

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
    } catch (_) { /* The warning was emitted during normalization above. */ }
  });

  const graph = [{
    '@type': 'Organization', '@id': ORGANIZATION_ID, name: 'The Biz Plans', url: SITE_URL,
    description: 'A Canadian business plan writing and consulting firm preparing business plans, financial projections and supporting research for financing, investment, acquisitions and growth.',
    logo: `${SITE_URL}img/bizplanlogo.png`, email: 'info@thebizplans.com', telephone: '+1-647-896-8362',
    address: {
      '@type': 'PostalAddress', streetAddress: '51 Burnhamill Pl', addressLocality: 'Toronto',
      addressRegion: 'ON', postalCode: 'M9C 3S3', addressCountry: 'CA'
    },
    founder: { '@id': PERSON_ID },
    sameAs: ['https://www.instagram.com/thebizplans/', 'https://www.facebook.com/people/The-biz-plans/61550125095965/', 'https://www.linkedin.com/company/thebizplans']
  }, {
    '@type': 'Person', '@id': PERSON_ID, name: 'Atul Jagga', url: `${SITE_URL}about-business-plan.html#atul-jagga`,
    jobTitle: 'Founder and Lead Consultant', worksFor: { '@id': ORGANIZATION_ID },
    knowsAbout: ['Business planning', 'Financial modelling', 'Market research', 'Business financing'],
    sameAs: ['https://www.linkedin.com/in/atul-jagga-68208827/']
  }];
  const addUnlessPresent = (node) => {
    const types = Array.isArray(node['@type']) ? node['@type'] : [node['@type']];
    if (!types.some((type) => existingTypes.has(type))) graph.push(node);
  };

  if (isHome) {
    addUnlessPresent({ '@type': 'WebSite', '@id': `${SITE_URL}#website`, url: SITE_URL, name: 'The Biz Plans', publisher: { '@id': ORGANIZATION_ID } });
  } else {
    // The current page intentionally has no `item`, matching its unlinked HTML state.
    graph.push({
      '@type': 'BreadcrumbList', '@id': `${pageUrl}#breadcrumb`,
      itemListElement: breadcrumbs.map((item, index) => ({
        '@type': 'ListItem', position: index + 1, name: item.name,
        ...(!item.current ? { item: item.url } : {})
      }))
    });
    const reviewedGuides = new Set([
      'canadian-bank-loan-business-plan-guide.html', 'how-banks-evaluate-business-plans.html',
      'royal-bank-of-canada.html', 'business-development-bank-of-canada.html',
      'canada-small-business-financing-program.html', 'td-canada-trust.html', 'scotiabank.html'
    ]);
    const isArticle = fileName.startsWith('blog-') || fileName.startsWith('chapter-') || reviewedGuides.has(fileName) || ogType === 'article';
    const isAbout = fileName === 'about-business-plan.html';
    const isService = /business-plan|services|financial-modeling|marketing-growth-strategy|pricing/.test(fileName) || /business plans?|business planning/i.test(pageName);
    if (isArticle) addUnlessPresent({ '@type': 'Article', '@id': `${pageUrl}#article`, headline: pageName, description, mainEntityOfPage: pageUrl, ...(ogImage ? { image: ogImage } : {}), author: { '@id': PERSON_ID }, reviewedBy: { '@id': PERSON_ID }, publisher: { '@id': ORGANIZATION_ID }, about: { '@id': ORGANIZATION_ID }, inLanguage: 'en-CA' });
    else if (isAbout) addUnlessPresent({ '@type': 'AboutPage', '@id': `${pageUrl}#webpage`, url: pageUrl, name: pageName, description, mainEntity: { '@id': ORGANIZATION_ID }, about: [{ '@id': ORGANIZATION_ID }, { '@id': PERSON_ID }], isPartOf: { '@id': `${SITE_URL}#website` }, inLanguage: 'en-CA' });
    else if (isService) addUnlessPresent({ '@type': 'Service', '@id': `${pageUrl}#service`, name: pageName, description, url: pageUrl, provider: { '@id': ORGANIZATION_ID }, areaServed: { '@type': 'Country', name: 'Canada' } });
    else addUnlessPresent({ '@type': 'WebPage', '@id': `${pageUrl}#webpage`, url: pageUrl, name: pageName, description, isPartOf: { '@id': `${SITE_URL}#website` }, about: { '@id': ORGANIZATION_ID }, inLanguage: 'en-CA' });
  }

  const schema = document.createElement('script');
  schema.type = 'application/ld+json';
  schema.textContent = JSON.stringify({ '@context': 'https://schema.org', '@graph': graph });
  document.head.appendChild(schema);
})();
