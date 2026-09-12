import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./generator.css";
const mount=document.getElementById("business-plan-generator-app");
if(mount) createRoot(mount).render(<StrictMode><App/></StrictMode>);
