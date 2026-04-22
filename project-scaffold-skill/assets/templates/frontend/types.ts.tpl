export type {{FeatureName}}ListParams = {
  search?: string;
};

export type {{FeatureName}}Item = {
  id: string;
  // TODO: add fields confirmed by backend schema and product requirements.
};

export type {{FeatureName}}ListResponse = {
  items: {{FeatureName}}Item[];
};
