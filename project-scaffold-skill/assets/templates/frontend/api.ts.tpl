import type { {{FeatureName}}ListParams, {{FeatureName}}ListResponse } from "./types";

const {{featureName}}BasePath = "{{api_path}}";

export async function fetch{{FeatureName}}List(
  params: {{FeatureName}}ListParams = {},
): Promise<{{FeatureName}}ListResponse> {
  const searchParams = new URLSearchParams();

  if (params.search) {
    searchParams.set("search", params.search);
  }

  const query = searchParams.toString();
  const response = await fetch(query ? `${{{featureName}}BasePath}?${query}` : {{featureName}}BasePath);

  if (!response.ok) {
    throw new Error("Failed to load {{feature_label}}.");
  }

  return response.json();
}
