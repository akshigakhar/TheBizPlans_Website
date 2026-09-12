import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./generator.css";

const rootElement = document.getElementById("business-plan-generator-app");

if (rootElement) {
  createRoot(rootElement).render(<StrictMode><App /></StrictMode>);
}
