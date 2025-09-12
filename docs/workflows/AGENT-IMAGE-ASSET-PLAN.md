# Agent Image Asset Refactoring Plan

**Date**: 2025-09-12
**Status**: In Progress

## 1. Objective

This document outlines the plan to refactor the agent profile markdown files. The initial implementation incorrectly embedded SVG image code directly into the markdown. This project will correct that by extracting the SVG code into separate `.svg` files and updating the markdown to use image references.

## 2. Directory Structure

A new root directory named `assets` will be created. This directory will mirror the agent folder structure to provide a clean, organized location for all image assets.

```
/assets/
├───1-product/
├───2-engineering/
├───3-operations/
└───4-thinktank/
```

## 3. SVG Design Principles

The stained-glass style SVGs will adhere to a consistent set of design principles:

- **Color Schemes**: Each of the four main agent categories has a distinct color palette to make them easily identifiable.
  - **1-product**: Blue & Gold
  - **2-engineering**: Green & Silver
  - **3-operations**: Red & Bronze
  - **4-thinktank**: Purple & White
- **Symbolism**: The central symbol within each SVG varies based on the agent's role and seniority, providing a quick visual cue to their function.
  - **Leadership Roles**: A complex, multi-layered star or compass.
  - **Senior Roles**: A simpler, solid diamond shape.
  - **Junior Roles**: A basic circular shape.
  - **Specialized Roles**: A standard square or a unique, representative shape (e.g., a triangle for First-Principles thinking).

## 4. Phased Implementation

The project will be executed in phases to ensure correctness and allow for verification.

- **Phase 1: Setup and Initial Implementation (Completed)**
- **Phase 2: Phased Rollout (In Progress)**
  - Create this documentation file.
  - Create the initial `assets` directory structure.
  - Refactor a single agent file (`001-strategy-product-leadership-guardian.md`) as a proof-of-concept.
  - Pause for user verification.

- **Phase 2: Phased Rollout (Pending)**
  - Process the remaining agent files in logical batches by category.

- **Phase 3: Final Documentation (Pending)**
  - Update all relevant project documentation to reflect the new asset structure.
