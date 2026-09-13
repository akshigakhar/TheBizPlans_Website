import { defineConfig } from "vite";
export default defineConfig({base:"/ai-generator-dist/",build:{outDir:"../ai-generator-dist",emptyOutDir:true,rollupOptions:{input:"src/main.jsx",output:{entryFileNames:"generator.js",chunkFileNames:"chunks/[name]-[hash].js",assetFileNames:({names})=>names.some(name=>name.endsWith(".css"))?"generator.css":"assets/[name]-[hash][extname]"}}}});
