import { use{{FeatureName}}List } from "./hooks";
import type { {{FeatureName}}Item } from "./types";

export function {{FeatureName}}Page() {
  const { data, error, isLoading, reload } = use{{FeatureName}}List();

  if (isLoading) {
    return <div>Loading {{feature_label}}...</div>;
  }

  if (error) {
    return (
      <section>
        <p>Unable to load {{feature_label}}.</p>
        <button type="button" onClick={reload}>
          Retry
        </button>
      </section>
    );
  }

  if (data.items.length === 0) {
    return <div>{/* TODO: replace with product empty state copy. */}No {{feature_label}} yet.</div>;
  }

  return (
    <section>
      <h1>{{FeatureTitle}}</h1>
      <ul>
        {data.items.map((item: {{FeatureName}}Item) => (
          <li key={item.id}>{/* TODO: render confirmed fields. */}{item.id}</li>
        ))}
      </ul>
    </section>
  );
}
