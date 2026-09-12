import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  base: "/ai-generator-dist/",
  build: {
    outDir: "../ai-generator-dist",
    emptyOutDir: true,
    rollupOptions: {
      input: "src/main.tsx",
      output: {
        entryFileNames: "generator.js",
        chunkFileNames: "chunks/[name]-[hash].js",
        assetFileNames: ({ names }) => names.some((name) => name.endsWith(".css")) ? "generator.css" : "assets/[name]-[hash][extname]"
      }
    }
  }
});
