export type Plan = {
  businessName: string; concept: string; customer: string; problem: string;
  market: string; advantage: string; marketing: string; operations: string;
  milestones: string; revenue: string; costs: string; funding: string;
};

export const emptyPlan: Plan = {
  businessName: "", concept: "", customer: "", problem: "", market: "", advantage: "",
  marketing: "", operations: "", milestones: "", revenue: "", costs: "", funding: ""
};
