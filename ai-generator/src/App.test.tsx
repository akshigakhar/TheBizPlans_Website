import "@testing-library/jest-dom/vitest";
import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import App from "./App";

describe("generator", () => {
  it("moves through the guided sections", () => {
    render(<App />);
    fireEvent.click(screen.getByRole("button", { name: "Save and continue" }));
    expect(screen.getByRole("group", { name: "Market" })).toBeInTheDocument();
  });
});
