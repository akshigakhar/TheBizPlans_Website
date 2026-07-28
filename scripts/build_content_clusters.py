#!/usr/bin/env python3
"""Insert consistent, crawlable commercial pathways into the static site.

The page lists are intentionally explicit: each URL has one role in the content model.
Run from anywhere; the script is idempotent between the marker comments.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- COMMERCIAL-PATHWAY:START -->'
END = '<!-- COMMERCIAL-PATHWAY:END -->'

LENDERS = {
    'canada-small-business-financing-program.html': ('Canada Small Business Financing Program', 'CSBFP financing'),
    'business-development-bank-of-canada.html': ('Business Development Bank of Canada', 'BDC financing'),
    'farm-credit-canada.html': ('Farm Credit Canada', 'FCC financing'),
    'canadian-agricultural-loans-act.html': ('Canadian Agricultural Loans Act', 'CALA financing'),
    'futurpreneur.html': ('Futurpreneur', 'Futurpreneur financing'),
    'black-entrepreneurship.html': ('Black Entrepreneurship Loan Fund', 'Black Entrepreneurship financing'),
    'vancity-business-plan.html': ('Vancity', 'Vancity business financing'),
    'royal-bank-of-canada.html': ('Royal Bank of Canada', 'RBC business financing'),
    'td-canada-trust.html': ('TD Canada Trust', 'TD business financing'),
    'scotiabank.html': ('Scotiabank', 'Scotiabank business financing'),
    'cibc.html': ('CIBC', 'CIBC business financing'),
    'national-bank-of-canada.html': ('National Bank of Canada', 'National Bank business financing'),
    'desjardins.html': ('Desjardins', 'Desjardins business financing'),
    'indigenous-aboriginal-entrepreneurship.html': ('Indigenous entrepreneurship financing programs', 'Indigenous business financing'),
    'women-entrepreneurship-loan-fund.html': ('Women Entrepreneurship Loan Fund', 'women entrepreneurship financing'),
    'export-development-canada.html': ('Export Development Canada', 'EDC financing and guarantees'),
    'private-lender-alternative-financing.html': ('Private and alternative lenders', 'alternative business financing'),
}

SERVICES = {
    'bank-loan-business-plans.html': ('Bank loan business plans', 'lenders and credit teams'),
    'investor-business-plan.html': ('Investor business plans', 'investors and capital partners'),
    'immigration-business-plans.html': ('Immigration business plans', 'immigration counsel and program reviewers'),
    'financial-modeling.html': ('Financial modelling', 'lenders, investors and management teams'),
    'strategic-business-plan.html': ('Strategic business plans', 'owners, boards and management teams'),
    'innovation-business-plan.html': ('Innovation business plans', 'funders, partners and management teams'),
    'business-plan-review.html': ('Business plan review', 'authors preparing for an external decision'),
    'marketing-growth-strategy.html': ('Marketing and growth strategy', 'owners, investors and operating teams'),
    'private-lender-alternative-financing.html': ('Alternative financing business plans', 'private lenders and financing partners'),
    'startup-visa-business-plan.html': ('Start-Up Visa business plans', 'designated organizations, counsel and reviewers'),
    'ict-business-plan.html': ('ICT business plans', 'counsel and immigration decision-makers'),
    'lmia-owner-operator-business-plan.html': ('C11 entrepreneur business plans', 'counsel and immigration decision-makers'),
    'self-employed-business-plan.html': ('Self-employed business plans', 'counsel and immigration decision-makers'),
}

BLOG_LINKS = {
    'executive': [('Investor business plans','investor-business-plan.html'),('Financial modelling','financial-modeling.html'),('Business plan examples','sample-other-plan.html')],
    'market': [('Strategic business plans','strategic-business-plan.html'),('Marketing and growth strategy','marketing-growth-strategy.html'),('Financial modelling','financial-modeling.html')],
    'swot': [('Strategic business plans','strategic-business-plan.html'),('Business plan review','business-plan-review.html'),('Case studies','case-studies.html')],
    'default': [('Business plan writing services','services.html'),('Business plan review','business-plan-review.html'),('Business plan examples','sample-other-plan.html')],
}

def read(path):
    with open(path, encoding='utf-8', newline='') as f: return f.read()

def write(path, text):
    newline = '\r\n' if '\r\n' in text else '\n'
    # New blocks are authored with LF; match the file convention.
    if newline == '\r\n':
        text = text.replace('\r\n', '\n').replace('\n', '\r\n')
    with open(path, 'w', encoding='utf-8', newline='') as f: f.write(text)

def replace_block(source, block):
    wrapped = f'{START}\n{block.strip()}\n{END}'
    pattern = re.compile(re.escape(START) + r'.*?' + re.escape(END), re.S)
    if pattern.search(source): return pattern.sub(wrapped, source)
    footer = re.search(r'\s*<footer\b', source, re.I)
    if not footer: raise ValueError('missing footer')
    return source[:footer.start()] + '\n\n' + wrapped + '\n\n' + source[footer.start():]

def lender_block(name, target):
    return f'''<section class="commercial-pathway py-5" aria-labelledby="business-plan-{slug(name)}">
  <div class="container">
    <div class="row g-5 align-items-start">
      <div class="col-lg-7">
        <p class="section-kicker">Business plan support</p>
        <h2 id="business-plan-{slug(name)}">Preparing a business plan for {name}</h2>
        <p class="lead">Program information is only the starting point. A financing request must show how the business will use capital, generate cash and manage repayment risk.</p>
        <h3 class="h5 mt-4">What a financing-ready plan should contain</h3>
        <ul class="check-list">
          <li>A specific funding request and itemized use of funds</li>
          <li>Market evidence, competitive positioning and a practical sales plan</li>
          <li>Operating assumptions linked to staffing, capacity and milestones</li>
          <li>Integrated profit-and-loss, cash-flow and balance-sheet projections</li>
          <li>Repayment capacity, owner contribution, sensitivities and key risks</li>
        </ul>
        <h3 class="h5 mt-4">Common weaknesses to correct before applying</h3>
        <p>Unsupported revenue forecasts, missing working capital, inconsistent numbers, unclear ownership contributions and a generic funding request can make a viable business difficult to assess. We test these connections before the plan is finalized.</p>
      </div>
      <div class="col-lg-5">
        <div class="conversion-card">
          <p class="section-kicker">The Biz Plans deliverables</p>
          <h3 class="h4">Turn {target} research into a decision-ready application</h3>
          <ol class="process-list">
            <li><strong>Scope:</strong> confirm the lender, request, timeline and available evidence.</li>
            <li><strong>Build:</strong> develop the narrative, research and integrated forecast.</li>
            <li><strong>Review:</strong> reconcile assumptions and prepare for lender questions.</li>
          </ol>
          <p><strong>Typical timing:</strong> confirmed after discovery based on complexity, data readiness and required research.</p>
          <div class="d-grid gap-2">
            <a class="btn btn-primary rounded-pill" href="project-brief.html">Get a Free Scope Assessment</a>
            <a class="btn btn-outline-primary rounded-pill" href="tel:+16478968362">Call +1 647-896-8362</a>
          </div>
        </div>
      </div>
    </div>
    <div class="topic-links mt-5" aria-label="Related business plan services">
      <a href="bank-loan-business-plans.html"><strong>Bank loan plans</strong><span>Core lender-ready service</span></a>
      <a href="financial-modeling.html"><strong>Financial modelling</strong><span>Cash flow and sensitivities</span></a>
      <a href="investor-business-plan.html"><strong>Investor plans</strong><span>Equity funding materials</span></a>
      <a href="case-studies.html"><strong>Case studies</strong><span>See representative work</span></a>
    </div>
    <p class="small text-muted mt-3 mb-0">The lender or program administrator—not The Biz Plans—makes all eligibility and credit decisions. Professional planning improves clarity; it does not guarantee financing.</p>
  </div>
</section>'''

def service_block(name, audience):
    return f'''<section class="commercial-pathway py-5" aria-labelledby="service-detail-{slug(name)}">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-7">
        <p class="section-kicker">What working together includes</p>
        <h2 id="service-detail-{slug(name)}">{name}: scope, process and deliverables</h2>
        <div class="row g-4 mt-1">
          <div class="col-md-6"><h3 class="h5">Who it is for</h3><p>Entrepreneurs and organizations preparing a documented case for {audience}.</p></div>
          <div class="col-md-6"><h3 class="h5">Deliverables</h3><p>A tailored narrative, cited market research, implementation plan and financial schedules appropriate to the engagement.</p></div>
          <div class="col-md-6"><h3 class="h5">Review process</h3><p>Discovery, evidence collection, drafting, financial reconciliation and a defined client review round before final delivery.</p></div>
          <div class="col-md-6"><h3 class="h5">Pricing and timing</h3><p>Quoted after scope review. Complexity, research depth, forecast requirements and source-data readiness determine the fee and schedule.</p></div>
        </div>
      </div>
      <div class="col-lg-5">
        <div class="conversion-card">
          <h3 class="h4">Start with the decision your plan must support</h3>
          <p>Tell us who will read the plan, what outcome you need, your deadline and which records are available. We will recommend a scope rather than forcing every project into one package.</p>
          <a class="btn btn-primary rounded-pill w-100 mb-2" href="project-brief.html">Request a Scope &amp; Quote</a>
          <a class="btn btn-outline-primary rounded-pill w-100" href="case-studies.html">Review Case Studies</a>
        </div>
      </div>
    </div>
    <div class="topic-links mt-5" aria-label="Related resources">
      <a href="financial-modeling.html"><strong>Financial modelling</strong><span>Forecasts and scenarios</span></a>
      <a href="sample-other-plan.html"><strong>Plan examples</strong><span>Understand the structure</span></a>
      <a href="faqs.html"><strong>Frequently asked questions</strong><span>Process and preparation</span></a>
      <a href="about-business-plan.html"><strong>Credentials &amp; review</strong><span>Who stands behind the work</span></a>
    </div>
  </div>
</section>'''

def blog_block(links):
    cards=''.join(f'<a href="{href}"><strong>{label}</strong><span>Explore the related service</span></a>' for label,href in links)
    return f'''<aside class="commercial-pathway py-5" aria-labelledby="next-step-heading">
  <div class="container">
    <div class="row g-4 align-items-center">
      <div class="col-lg-8"><p class="section-kicker">Put the guidance to work</p><h2 id="next-step-heading">Build the next section of your business plan</h2><p>Use this article as an educational starting point, then connect the analysis to a coherent strategy and financial model. If the plan will be reviewed by a lender, investor or immigration decision-maker, we can help test the evidence and assumptions.</p></div>
      <div class="col-lg-4 text-lg-end"><a class="btn btn-primary rounded-pill px-4" href="project-brief.html">Discuss Your Business Plan</a></div>
    </div>
    <div class="topic-links mt-4">{cards}<a href="contact.html"><strong>Contact</strong><span>Ask a project question</span></a></div>
  </div>
</aside>'''

def slug(value):
    return re.sub(r'[^a-z0-9]+','-',value.lower()).strip('-')

# Financing pages are maintained by build_financing_pages.py because each one
# requires lender-specific underwriting, projection, document and FAQ content.
FINANCING_MANAGED=set(LENDERS) | {'bank-loan-business-plans.html'}
for filename,(name,audience) in SERVICES.items():
    if filename in FINANCING_MANAGED: continue
    path=ROOT/filename
    write(path, replace_block(read(path), service_block(name,audience)))

for path in ROOT.glob('blog-*.html'):
    if path.name == 'blog-learning-hub.html': continue
    key='default'
    for candidate in ('executive','market','swot'):
        if candidate in path.stem: key=candidate; break
    write(path, replace_block(read(path), blog_block(BLOG_LINKS[key])))

print(f'Updated non-financing service pages and {len(list(ROOT.glob("blog-*.html")))-1} articles. Run build_financing_pages.py for financing pages.')
