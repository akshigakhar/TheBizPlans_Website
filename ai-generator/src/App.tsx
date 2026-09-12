import { useEffect, useState } from "react";
import { track } from "./analytics";
import { emptyPlan, type Plan } from "./types";

const STORAGE_KEY = "thebizplans.generator.plan.v1";
const sections = [
  { title: "Business", fields: [["businessName", "Business name", "text"], ["concept", "What does your business offer?", "textarea"], ["problem", "What customer problem do you solve?", "textarea"]] },
  { title: "Market", fields: [["customer", "Who is your ideal customer?", "textarea"], ["market", "Describe your market and its demand", "textarea"], ["advantage", "Why will customers choose you?", "textarea"]] },
  { title: "Operations", fields: [["marketing", "How will you reach and retain customers?", "textarea"], ["operations", "How will the business operate day to day?", "textarea"], ["milestones", "What are your next three milestones?", "textarea"]] },
  { title: "Financials", fields: [["revenue", "How will the business earn revenue?", "textarea"], ["costs", "What are the main startup and operating costs?", "textarea"], ["funding", "How much funding is needed and how will it be used?", "textarea"]] }
] as const;

const readSaved = (): Plan => {
  try { return { ...emptyPlan, ...JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}") }; }
  catch { return emptyPlan; }
};

export default function App() {
  const [plan, setPlan] = useState<Plan>(readSaved);
  const [step, setStep] = useState(0);
  const [generated, setGenerated] = useState(false);
  const section = sections[step];

  useEffect(() => { localStorage.setItem(STORAGE_KEY, JSON.stringify(plan)); }, [plan]);
  const setValue = (key: keyof Plan, value: string) => setPlan((current) => ({ ...current, [key]: value }));
  const move = (next: number) => {
    if (next > step) track("section_completed", section.title.toLowerCase());
    setStep(next); setGenerated(false); window.location.hash = `generator-${next + 1}`;
  };
  const generate = () => { setGenerated(true); track("plan_generated"); };
  const clear = () => { if (window.confirm("Clear your saved answers and start again?")) { setPlan(emptyPlan); setStep(0); setGenerated(false); localStorage.removeItem(STORAGE_KEY); } };

  return <div className="generator-shell">
    <div className="generator-intro">
      <div><span className="generator-badge">Free to use · saved on this device</span><h2>Build your business plan draft</h2><p>Answer the guided questions. Your information stays in this browser and is not sent to analytics.</p></div>
      <button className="generator-link-button" type="button" onClick={clear}>Start over</button>
    </div>
    <nav className="generator-progress" aria-label="Generator progress">
      {sections.map((item, index) => <button type="button" key={item.title} className={index === step ? "is-active" : ""} aria-current={index === step ? "step" : undefined} onClick={() => move(index)}><span>{index + 1}</span>{item.title}</button>)}
    </nav>
    {!generated ? <form className="generator-form" onSubmit={(event) => { event.preventDefault(); if (step < sections.length - 1) move(step + 1); else generate(); }} onFocus={() => track("generator_started")}>
      <fieldset><legend>{section.title}</legend><p className="generator-help">Be specific, use evidence where possible, and review every assumption before sharing your plan.</p>
        <div className="generator-fields">{section.fields.map(([key, label, kind]) => <label key={key}>{label}{kind === "textarea" ? <textarea rows={4} value={plan[key]} onChange={(event) => setValue(key, event.target.value)} placeholder="Enter your answer…" /> : <input value={plan[key]} onChange={(event) => setValue(key, event.target.value)} placeholder="Enter your answer…" />}</label>)}</div>
      </fieldset><div className="generator-actions">{step > 0 && <button className="generator-button generator-button-secondary" type="button" onClick={() => move(step - 1)}>Back</button>}<button className="generator-button" type="submit">{step === sections.length - 1 ? "Create my draft" : "Save and continue"}</button></div>
    </form> : <PlanDraft plan={plan} onEdit={() => setGenerated(false)} />}
  </div>;
}

function PlanDraft({ plan, onEdit }: { plan: Plan; onEdit: () => void }) {
  const blocks = [["Executive summary", plan.concept], ["Customer need", plan.problem], ["Target market", `${plan.customer}\n\n${plan.market}`], ["Competitive advantage", plan.advantage], ["Marketing and sales", plan.marketing], ["Operations", plan.operations], ["Milestones", plan.milestones], ["Revenue model", plan.revenue], ["Costs and funding", `${plan.costs}\n\n${plan.funding}`]];
  return <section className="generator-draft" aria-live="polite"><div className="generator-draft-heading"><div><span className="generator-badge">First draft</span><h3>{plan.businessName || "Your business plan"}</h3></div><div className="generator-actions"><button type="button" className="generator-button generator-button-secondary" onClick={onEdit}>Edit answers</button><button type="button" className="generator-button" onClick={() => { track("plan_downloaded"); window.print(); }}>Print / save PDF</button></div></div>
    <p className="generator-notice"><strong>Review required:</strong> Verify all facts and assumptions. This draft does not guarantee financing or approval.</p>
    {blocks.map(([title, content]) => <article key={title}><h4>{title}</h4><p>{content || "Not provided — return to the questions to complete this section."}</p></article>)}</section>;
}
