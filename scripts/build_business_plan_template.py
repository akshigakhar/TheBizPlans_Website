#!/usr/bin/env python3
"""Rebuild downloads/canadian-business-plan-template.pdf from the repo root. Requires ReportLab."""
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

sections = [
('Executive summary', 'Write this last. Summarize your business, location, customer problem, solution, competitive advantage, milestones and financial outlook. State the funding purpose and repayment case if applicable.'),
('Company overview', 'Enter the legal and trading names, province or territory, registration status, ownership percentages, business address and stage of development. Explain the mission, history, objectives and measurable milestones. Identify permits and regulatory requirements to verify.'),
('Products and services', 'Describe each offering, the customer benefit, pricing basis, delivery method and direct costs. Explain differentiation, intellectual property, suppliers, product development and any dependencies or limitations.'),
('Market analysis', 'Define the target customer and geography. Record current research sources, dates and limitations. TAM (total addressable market): estimate total relevant demand using a documented method. SAM (serviceable available market): narrow demand to the customers and geography you can serve. SOM (serviceable obtainable market): justify a realistic share using acquisition capacity, competition and delivery limits. Use consistent units and periods; distinguish evidence from assumptions. Compare competitors, substitutes, demand trends, barriers and key risks.'),
('Marketing and sales plan', 'Explain positioning, channels, promotion, sales process and customer retention. Assign activities, budgets, owners and dates. Document lead volumes, conversion assumptions, sales cycle, acquisition costs and payment terms. Link sales targets to the revenue assumptions and test how slower sales affect cash.'),
('Operations plan', 'Describe premises, equipment, technology, suppliers, inventory, workflow, quality controls and customer delivery. Set capacity, opening hours, staffing needs, implementation dates and responsibilities. Identify insurance, licences, compliance checks, continuity arrangements and mitigations for operating risks.'),
('Management and organisation', 'List owners, management roles, relevant experience, responsibilities and decision rights. Outline the organisation chart, hiring schedule, compensation, advisers, skill gaps and succession or contingency arrangements. Link staffing costs to the financial plan.'),
('Financial plan', 'Use CAD unless you clearly state another currency. Define the forecast start date, accounting basis, tax treatment, owner compensation, inflation, payment timing and borrowing terms. Build calculations in a spreadsheet; these blank tables do not calculate totals. Support costs with dated quotes and research. Add monthly cash flow for the first year and any schedules required by your reader. Reconcile income, cash flow, balance sheets and funding; test a downside case.'),
('Funding request', 'If funding is needed, specify the amount, proposed debt or equity, timing and exact uses. Separate confirmed owner funds from requested or conditional financing. Match sources to startup costs and working capital; explain repayment capacity and downside risks. Describe security only where relevant and verified. For CSBFP or BDC, confirm current eligibility, lender forms and evidence requirements directly; this template does not establish approval. If no external funding is sought, explain how the business will be financed.'),
('Appendix checklist', 'Attach only relevant, current evidence and cross-reference it from the plan. Record the document date, source and appendix reference. Protect personal and confidential information. Check the intended lender or immigration program requirements before submission.')]
styles=getSampleStyleSheet()
styles['Normal'].fontSize=10
styles['Normal'].leading=15
styles['Title'].textColor=colors.HexColor('#173d64')
story=[]
def p(s,style='Normal'): story.append(Paragraph(s,styles[style])); story.append(Spacer(1,10))
def table(headers, rows, widths=None):
    data=[[Paragraph(str(c),styles['Normal']) for c in headers]]+[[Paragraph(str(c),styles['Normal']) for c in row] for row in rows]
    t=Table(data,colWidths=widths or [480/len(headers)]*len(headers),repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eef3f8')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#a0aab4')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.append(t); story.append(Spacer(1,14))
def lines(n=12): table(['Your notes / draft'], [[' ']]*n,[480])
p('The Biz Plans','Title'); p('Canadian Business Plan TEMPLATE','Title'); p('Blank framework with guidance — replace every prompt with your own evidence.')
table(['Cover page field','Complete with your details'],[[x,''] for x in ['Business / legal name','Business address and province / territory','Prepared by and role','Contact details','Prepared for / intended reader','Plan date and version','Forecast period / currency']],[225,255])
p('thebizplans.com'); p('Free to download. No email, signup or purchase required. Print and write in the spaces or recreate the structure in your editor. This PDF is not a fillable form. No business facts or financial figures have been supplied.'); story.append(PageBreak())
p('Table of contents placeholder','Heading1'); p('After completing and formatting your plan, enter the final page numbers. Update these whenever the document changes.')
table(['Section','Final page'],[[f'{i}. {name}',''] for i,(name,_) in enumerate(sections,1)],[385,95]); p('Using this template','Heading2'); p('Confirm your reader’s requirements first. Research and draft the sections, calculate linked financial statements, then write the executive summary. Remove guidance before submitting. A template is a starting structure; lenders and immigration programs judge your content and supporting evidence, and may require additional documents.'); story.append(PageBreak())
for i,(name,prompt) in enumerate(sections,1):
    p(f'{i}. {name}','Heading1'); p(prompt)
    if name=='Financial plan':
        p('Startup costs and opening funding needs','Heading2'); table(['Cost / use of funds','CAD amount','Quote / source / date'],[[r,'',''] for r in ['Registration, permits and professional fees','Premises, deposits and leasehold improvements','Equipment and technology','Opening inventory and supplies','Pre-opening payroll and marketing','Opening working capital reserve','Contingency (explain basis)','Other (specify)','Total startup requirement']],[220,90,170])
        story.append(PageBreak()); p('Revenue assumptions','Heading1'); p('Use one row per revenue stream. Specify the unit (jobs, units, subscriptions or billable hours), period, capacity ceiling, seasonality, collection timing and evidence. Revenue = volume × price; distinguish sales from cash receipts.')
        table(['Stream / unit','Price (CAD)','Volume / period','Evidence / timing'],[['','','','']]*7,[140,80,110,150]); p('Assumptions and downside scenario','Heading2'); lines(8)
        for title,rows in [
          ('Projected income statement',['Revenue','Direct costs / cost of sales','Gross profit','Payroll and benefits','Occupancy','Marketing','Other operating expenses','Depreciation / amortisation','Operating profit','Interest expense','Income tax','Net income']),
          ('Projected cash flow',['Opening cash','Customer receipts','Supplier / operating payments','Payroll payments','Tax payments','Capital expenditures','Loan proceeds','Owner equity contributions','Interest payments','Loan principal repayments','Owner distributions','Net change in cash','Closing cash']),
          ('Projected balance sheet',['Cash','Accounts receivable','Inventory','Other current assets','Fixed assets, net','Total assets','Accounts payable','Tax payable','Current debt portion','Long-term debt','Other liabilities','Total liabilities','Owner equity contributed','Retained earnings','Total equity','Total liabilities and equity'])]:
            story.append(PageBreak()); p(title,'Heading1'); p('Enter forecast years and values in CAD. All financial value cells are intentionally blank. Add rows as needed. Cash flow closing cash must match balance sheet cash; assets must equal liabilities plus equity. Retained earnings must reconcile to profits and distributions.'); table(['Line item','Year 1','Year 2','Year 3'],[[r,'','',''] for r in rows],[240,80,80,80])
    elif name=='Appendix checklist':
        table(['Check','Evidence to consider','Reference / date'],[['',r,''] for r in ['Owner and management CVs','Registration and ownership documents','Market sources and customer research','Competitor analysis and pricing evidence','Supplier quotations and equipment budgets','Lease or premises documentation','Licences, permits and insurance','Sales contracts or letters of intent (label status)','Detailed forecast workbook and assumptions','Funding sources and lender documents','Program-specific immigration evidence (if applicable)','Risk register and implementation timeline']],[45,300,135])
    else: lines(15 if name!='Market analysis' else 12)
    if i<len(sections): story.append(PageBreak())
def footer(c,doc):
    c.setFont('Helvetica',8); c.setFillColor(colors.HexColor('#173d64')); c.drawString(54,30,'The Biz Plans | thebizplans.com | Business Plan TEMPLATE'); c.drawRightString(558,30,str(doc.page))
SimpleDocTemplate('downloads/canadian-business-plan-template.pdf',pagesize=letter,rightMargin=54,leftMargin=54,topMargin=50,bottomMargin=50,title='Canadian Business Plan Template',author='The Biz Plans').build(story,onFirstPage=footer,onLaterPages=footer)
