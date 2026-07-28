#!/usr/bin/env python3
"""Build a visible, page-specific FAQ and matching FAQPage JSON-LD on every page.

The generated copy is deliberately grouped by page intent rather than repeated sitewide.
Run this script after adding or renaming a top-level HTML page. Existing generated blocks
are replaced between markers, making the script safe to run more than once.
"""
from html import escape, unescape
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- PAGE-FAQ:START -->"
END = "<!-- PAGE-FAQ:END -->"


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", value))).strip()


def page_topic(source: str, filename: str) -> str:
    match = re.search(r"<h1\b[^>]*>(.*?)</h1>", source, re.I | re.S)
    topic = clean_text(match.group(1)) if match else filename.removesuffix(".html").replace("-", " ").title()
    # Questions read more naturally without common promotional qualifiers.
    topic = re.sub(r"^(Professional|Lender-Ready)\s+", "", topic, flags=re.I)
    return topic.rstrip(".?!")


def classify(filename: str) -> str:
    if filename.startswith("blog-") or filename.startswith("chapter-") or filename in {"books.html", "business-plan-essentials.html", "authoritative-resources.html"}:
        return "learning"
    if filename in {"privacy-policy.html", "terms.html", "refund-policy.html", "editorial-policy.html"}:
        return "policy"
    if filename in {"contact.html", "project-brief.html", "pricing.html", "about-business-plan.html", "services.html", "index.html", "case-studies.html"}:
        return "company"
    if "sample" in filename:
        return "sample"
    if filename.endswith("business-plan-writers.html"):
        return "location"
    if any(word in filename for word in ("immigration", "pnp", "visa", "lmia", "self-employed", "entrepreneur-business-plan")):
        return "immigration"
    if any(word in filename for word in ("bank", "loan", "financ", "credit", "futurpreneur", "scotiabank", "cibc", "desjardins", "vancity")):
        return "financing"
    if filename.endswith("business-plans.html") or filename in {"indigenous-business-plan.html", "telecom-business-plans.html"}:
        return "industry"
    return "service"


def questions(kind: str, topic: str):
    sets = {
        "learning": [
            (f"What is the main takeaway from {topic}?", f"The central lesson is to turn the topic into evidence, decisions and measurable assumptions rather than treating it as stand-alone prose. Apply it consistently across the market, operating and financial sections of the plan."),
            (f"How does {topic} fit into a complete business plan?", "It should support the plan's overall logic: a defined customer need leads to a practical strategy, operating requirements and financial results. Review connected sections after making changes so the document does not contradict itself."),
            ("What evidence should support this part of the plan?", "Use current, traceable sources appropriate to the claim, such as government data, industry publications, direct operating records and documented customer or competitor research. Label estimates and explain how they were calculated."),
            ("Which mistakes reduce credibility?", "Common problems include generic claims, outdated statistics, unsupported market-share assumptions and numbers that do not match the written strategy. Specific sources and a clear chain of reasoning are more persuasive than excessive detail."),
            ("How should this guidance be adapted for a lender or investor?", "A lender generally emphasizes repayment capacity, cash flow and downside protection, while an investor also evaluates growth, differentiation and potential return. Keep the underlying facts consistent while prioritizing the reader's decision criteria."),
            ("When should this section be updated?", "Update it when pricing, customers, competition, funding needs or operating assumptions materially change. It should also be reviewed immediately before submission so dates, sources and financial figures remain aligned."),
        ],
        "financing": [
            (f"What should a business plan for {topic} include?", "Include the amount requested, an itemized use of funds, owner contribution, market evidence, operating plan and integrated financial projections. The assumptions should demonstrate how the business expects to generate enough cash to meet its obligations."),
            ("How many years of financial projections are normally useful?", "A monthly cash-flow view for the near term and annual projections for later years are often useful, but the appropriate period depends on the lender, program and business stage. Confirm the recipient's current requirements before submitting."),
            ("Does a strong business plan guarantee financing approval?", "No. The lender or program makes its own eligibility, credit and security decisions. A well-supported plan helps reviewers understand the opportunity and risks, but it cannot guarantee approval or a particular financing amount."),
            ("What documents should support the financing request?", "Depending on the application, useful records may include owner résumés, quotes, leases, historical statements, tax records, debt schedules, licenses and evidence of equity. Provide only documents relevant to the reviewer and verify current requirements directly."),
            ("How should repayment risk be addressed?", "Show realistic margins, working-capital needs, debt payments and cash timing. Include sensitivities for important variables such as slower sales, lower pricing or higher costs, then explain the actions management could take."),
            ("When should the plan be reviewed before submission?", "Review it after the funding structure and supporting quotes are known, and again immediately before submission. Reconcile every funding figure across the narrative, cash flow, balance sheet and use-of-funds schedule."),
        ],
        "immigration": [
            (f"What should a plan for {topic} demonstrate?", "It should present a credible Canadian business concept, the applicant's role, market evidence, implementation milestones, staffing and financially consistent projections. The exact emphasis depends on the current program and the facts of the application."),
            ("Is an immigration business plan the same as a bank plan?", "No. Both require commercial credibility, but an immigration plan must also address the relevant program criteria and show how the applicant will actively implement the venture. A bank plan places greater emphasis on credit and repayment."),
            ("How is the applicant's experience reflected in the plan?", "The plan should connect relevant ownership, management and industry experience to specific responsibilities and execution risks. It should not claim qualifications that are not supported by the applicant's documents."),
            ("What research makes the proposal more credible?", "Use Canadian market, competitor, pricing, location and regulatory evidence that matches the actual launch geography. Sources should be current, cited and connected to forecast assumptions rather than added as general background."),
            ("Can a business plan guarantee an immigration decision?", "No. Government officers and other authorized organizations make all eligibility and application decisions. A professional plan can improve clarity and consistency but cannot guarantee endorsement, nomination, a work permit or permanent residence."),
            ("Who should review the plan before filing?", "The applicant should verify every factual statement and financial assumption. Regulated immigration counsel should review legal and program matters, while accounting or industry advisers may be appropriate for specialized financial and operating claims."),
        ],
        "industry": [
            (f"What makes {topic} different from a generic business plan?", "An industry-specific plan reflects the venture's real revenue drivers, capacity limits, cost structure, regulations and customer buying process. Replacing labels in a generic template does not provide that operating detail."),
            ("Which market research should be included?", "Define the actual customer and service geography, estimate demand with cited sources, compare relevant competitors and explain how buyers choose. Connect the findings directly to pricing, sales volume and marketing assumptions."),
            ("How should revenue be forecast?", "Build revenue from measurable drivers such as customers, units, contracts, utilization or average transaction value. Explain ramp-up timing and test the result against capacity and credible market demand."),
            ("Which operating costs are commonly overlooked?", "Working capital, insurance, compliance, maintenance, professional fees, customer acquisition and hiring ramp-up are frequently understated. The relevant costs vary by industry, so document quotes and assumptions where possible."),
            ("What risks should the plan address?", "Prioritize risks that could materially affect demand, delivery, margins, staffing or compliance. For each significant risk, describe a practical mitigation or contingency rather than relying on a generic risk list."),
            ("Can the same plan be used for lenders and investors?", "The factual foundation can be shared, but the presentation should match the audience. Lenders focus on repayment and downside protection; investors also examine growth, defensibility, management and return potential."),
        ],
        "sample": [
            (f"What can readers learn from {topic}?", "Use the sample to understand structure, level of detail and the connection between strategy and financial assumptions. It is an illustration, not a substitute for evidence about a different business."),
            ("Can this sample be copied for a real application?", "No. Copying creates unsupported claims and usually fails to reflect the applicant, market, funding request and operating model. Use it as a planning reference and build the actual document from verified facts."),
            ("Which sections should be customized first?", "Start with the audience, funding objective, customer, location, business model and management team. Those decisions shape the market research, operations, milestones, risks and forecast."),
            ("How should sample financial figures be used?", "Treat them only as examples of presentation. Develop projections from the real venture's pricing, volume, staffing, capital spending and cash timing, and retain support for each material assumption."),
            ("How can a sample help improve plan quality?", "It can provide a checklist for missing sections and show how information flows through a document. Quality ultimately depends on relevant evidence, internal consistency and fitness for the intended reader."),
            ("When is professional review useful?", "Review is useful when the plan supports a consequential financing, investment or immigration decision, or when the forecast is complex. An independent reviewer can identify gaps and inconsistencies before submission."),
        ],
        "location": [
            (f"What should {topic} say about the local market?", "The plan should define the real trading area, local customer segments, direct competitors, pricing, labour conditions and premises needs. The research boundary may be a neighbourhood, metro area, province or wider market depending on how the business sells."),
            ("Do business plan projects require in-person meetings?", "Not necessarily. Structured interviews, secure document exchange and review calls can support an effective remote process. Any on-site research or meeting requirement should be confirmed when the project is scoped."),
            ("Can the plan be prepared for a local bank or credit union?", "Yes, provided the scope reflects the intended institution and its current requirements. The final financing decision remains with the lender, and applicants should confirm required forms and supporting documents directly."),
            ("How are local competitors evaluated?", "Identify competitors that serve the same customer and geography, then compare offer, pricing, access, reputation and positioning. The goal is to support a realistic strategy, not simply list nearby businesses."),
            ("Should local costs appear in the forecast?", "Yes. Use location-appropriate assumptions for rent, wages, logistics, insurance, licensing and customer acquisition where they are material. Quotes and documented benchmarks improve reliability."),
            ("What information is helpful to start?", "Provide the plan audience, deadline, location, customer profile, funding target and available operating or financial records. Early clarity about missing evidence makes the research and review process more efficient."),
        ],
        "policy": [
            (f"What does {topic} cover?", "This page explains the applicable website or service policy in plain language. Read the complete policy because headings and FAQs are summaries and do not replace the governing terms on the page."),
            ("Who does this policy apply to?", "It applies as described in the policy text, including any stated distinctions between website visitors, prospective clients and clients. Contact The Biz Plans if your circumstances are not addressed clearly."),
            ("Does this FAQ replace the full policy?", "No. The full policy controls. These questions help readers locate common topics, but they do not add to, remove or amend the policy language."),
            ("How can I ask a question about this policy?", "Use the contact details shown on this website and identify the policy and issue in question. Do not send unnecessary confidential or sensitive information in an initial message."),
            ("Can this policy change?", "The policy may be updated as practices or requirements change. Review the version available on the website when you use the site or engage a service."),
            ("Where can I find related policies?", "Links to privacy, terms and refund information appear in the website footer. Read all policies relevant to your interaction or engagement rather than relying on one page in isolation."),
        ],
        "company": [
            (f"Who is {topic} intended for?", "It is designed for entrepreneurs and organizations that need clear, evidence-based business planning support. The appropriate service and deliverables depend on the decision-maker, business stage, available records and deadline."),
            ("What information is needed to begin?", "Share the intended reader, purpose, deadline, business model, funding target and available financial or operating records. A concise initial brief helps identify the right scope and any evidence gaps."),
            ("Are services based on a standard template?", "A consistent quality-control structure may be used, but the research, strategy, assumptions and financial model should reflect the individual venture and audience. Generic copy is not a substitute for verified client information."),
            ("How are project timing and fees determined?", "They depend on scope, complexity, research depth, forecast requirements, data readiness and review needs. Confirm the current quote, deliverables and schedule before work begins."),
            ("Can business planning guarantee funding or approval?", "No. Banks, investors, government bodies and other reviewers make independent decisions. Professional support can make a submission clearer and more consistent, but it cannot guarantee an outcome."),
            ("How is quality checked before delivery?", "The narrative and financial schedules are reviewed for consistency, material claims are tied to appropriate evidence, and client-supplied facts require client verification. The exact review steps depend on the engagement scope."),
        ],
        "service": [
            (f"What does {topic} include?", "The scope is tailored to the decision the work must support and may include discovery, market evidence, strategy, operating assumptions, financial analysis and review. Confirm the specific deliverables in the project proposal."),
            ("Who is this service best suited for?", "It is most useful when an owner or organization needs a structured, evidence-based document for planning or an external decision. The intended reader and stage of the business determine the appropriate depth."),
            ("What should a client prepare before starting?", "Prepare the objective, deadline, ownership and management details, product or service information, available research and financial records. Identify estimates clearly so they can be tested rather than presented as facts."),
            ("How are financial assumptions developed?", "Assumptions should be built from pricing, demand, capacity, staffing, cost quotes and cash timing. Material inputs are documented and reconciled across the narrative and financial schedules."),
            ("How long does the work take?", "Timing varies with complexity, research needs, source-data readiness and review cycles. A realistic schedule can be confirmed only after the required deliverables and available information are assessed."),
            ("Does professional support guarantee a successful outcome?", "No. The relevant lender, investor, government body or management team makes the decision. Professional work improves clarity and analytical consistency but does not guarantee approval, funding or performance."),
        ],
    }
    return sets[kind]


def build_block(filename: str, topic: str, items) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", filename.removesuffix(".html").lower()).strip("-")
    cards = []
    for number, (question, answer) in enumerate(items, 1):
        cards.append(f'''      <div class="col-lg-6">
        <details class="h-100 border rounded p-4 bg-white"{' open' if number == 1 else ''}>
          <summary class="fw-bold text-dark">{escape(question)}</summary>
          <p class="mt-3 mb-0">{escape(answer)}</p>
        </details>
      </div>''')
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items],
    }
    return f'''{START}
<section class="page-faq py-5 bg-light" aria-labelledby="{slug}-faq-heading">
  <div class="container">
    <div class="text-center mx-auto mb-5" style="max-width: 760px;">
      <p class="section-kicker">Helpful answers</p>
      <h2 id="{slug}-faq-heading">Frequently asked questions about {escape(topic)}</h2>
      <p class="mb-0">Practical answers to help you evaluate this topic and prepare your next step.</p>
    </div>
    <div class="row g-4">
{chr(10).join(cards)}
    </div>
  </div>
</section>
<script type="application/ld+json" data-page-faq>{json.dumps(schema, ensure_ascii=False, separators=(',', ':'))}</script>
{END}'''


def update(source: str, block: str) -> str:
    footer = re.search(r"^[ \t]*<footer\b[^\n]*(\r?\n)", source, re.I | re.M)
    if not footer:
        raise ValueError("missing footer")
    newline = footer.group(1)
    if newline == "\r\n":
        block = block.replace("\n", "\r\n")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if pattern.search(source):
        return pattern.sub(block, source)
    return source[:footer.start()] + block + newline + source[footer.start():]


updated = 0
for path in sorted(ROOT.glob("*.html")):
    # The dedicated FAQ page already has 12 curated questions and FAQPage schema.
    if path.name == "faqs.html":
        continue
    with path.open(encoding="utf-8", newline="") as handle:
        source = handle.read()
    topic = page_topic(source, path.name)
    source = update(source, build_block(path.name, topic, questions(classify(path.name), topic)))
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(source)
    updated += 1

print(f"Built six page-specific FAQs on {updated} pages; retained the curated FAQ hub.")
