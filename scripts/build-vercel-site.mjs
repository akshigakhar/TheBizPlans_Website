import { cp, mkdir, readdir, rm } from "node:fs/promises";
import { extname, join } from "node:path";

const root = new URL("../", import.meta.url);
const outputDirectory = process.argv[2] || "site-dist";
if (outputDirectory.startsWith("/") || outputDirectory.split("/").includes("..")) {
  throw new Error("The output directory must be a safe repository-relative path.");
}
const destination = new URL(`../${outputDirectory.replace(/\/?$/, "/")}`, import.meta.url);
const publicDirectories = ["ai-generator-dist", "css", "downloads", "img", "js", "lib", "swot-analysis-business-plan"];
const publicRootExtensions = new Set([".html", ".txt", ".xml"]);

await rm(destination, { recursive: true, force: true });
await mkdir(destination, { recursive: true });

for (const directory of publicDirectories) {
  await cp(new URL(`../${directory}/`, import.meta.url), new URL(`${directory}/`, destination), {
    recursive: true
  });
}

for (const entry of await readdir(root, { withFileTypes: true })) {
  if (entry.isFile() && publicRootExtensions.has(extname(entry.name))) {
    await cp(join(root.pathname, entry.name), join(destination.pathname, entry.name));
  }
}

console.log(`Staged the static website in ${outputDirectory} for Vercel.`);
