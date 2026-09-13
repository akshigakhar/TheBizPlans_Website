export type GeneratorEvent = "generator_started" | "section_completed" | "plan_generated" | "plan_downloaded";

export function track(event: GeneratorEvent, section?: string) {
  const win = window as Window & { dataLayer?: Record<string, string>[] };
  if (!Array.isArray(win.dataLayer)) return;
  win.dataLayer.push(section ? { event, generator_section: section } : { event });
}
