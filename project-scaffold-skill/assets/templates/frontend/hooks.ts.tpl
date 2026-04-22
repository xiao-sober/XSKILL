import { useCallback, useEffect, useState } from "react";

import { fetch{{FeatureName}}List } from "./api";
import type { {{FeatureName}}ListParams, {{FeatureName}}ListResponse } from "./types";

type Use{{FeatureName}}ListState = {
  data: {{FeatureName}}ListResponse;
  error: Error | null;
  isLoading: boolean;
};

const initialState: Use{{FeatureName}}ListState = {
  data: { items: [] },
  error: null,
  isLoading: true,
};

const default{{FeatureName}}ListParams: {{FeatureName}}ListParams = {};

export function use{{FeatureName}}List(params: {{FeatureName}}ListParams = default{{FeatureName}}ListParams) {
  const [state, setState] = useState<Use{{FeatureName}}ListState>(initialState);

  const load = useCallback(async () => {
    setState((current) => ({ ...current, error: null, isLoading: true }));

    try {
      const data = await fetch{{FeatureName}}List(params);
      setState({ data, error: null, isLoading: false });
    } catch (error) {
      setState({
        data: { items: [] },
        error: error instanceof Error ? error : new Error("Failed to load {{feature_label}}."),
        isLoading: false,
      });
    }
  }, [params]);

  useEffect(() => {
    void load();
  }, [load]);

  return {
    ...state,
    reload: load,
  };
}
