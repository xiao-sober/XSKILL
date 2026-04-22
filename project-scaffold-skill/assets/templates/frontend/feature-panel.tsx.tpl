import type { {{FeatureName}}Item } from "../types";

type {{FeatureName}}PanelProps = {
  item: {{FeatureName}}Item;
};

export function {{FeatureName}}Panel({ item }: {{FeatureName}}PanelProps) {
  return (
    <article>
      {/* TODO: render confirmed {{feature_label}} fields. */}
      <h2>{item.id}</h2>
    </article>
  );
}
