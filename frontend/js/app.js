/**
 * Application frontale en JavaScript « vanilla » (sans framework).
 * Notions utilisées : sélection du DOM, boucles, template literals,
 * écouteurs d'événements. Les données ci-dessous seront remplacées par
 * des appels fetch() vers le backend Python une fois disponible.
 */

const SAMPLE_METRICS = [
  {
    id: "logistic_regression",
    label: "Régression logistique",
    accuracy: 0.82,
    precision: 0.79,
    recall: 0.76,
    f1: 0.775,
  },
  {
    id: "knn",
    label: "KNN",
    accuracy: 0.8,
    precision: 0.77,
    recall: 0.74,
    f1: 0.755,
  },
  {
    id: "decision_tree",
    label: "Arbre de décision",
    accuracy: 0.78,
    precision: 0.75,
    recall: 0.73,
    f1: 0.74,
  },
  {
    id: "random_forest",
    label: "Random Forest",
    accuracy: 0.85,
    precision: 0.83,
    recall: 0.81,
    f1: 0.82,
  },
  {
    id: "svm",
    label: "SVM",
    accuracy: 0.83,
    precision: 0.81,
    recall: 0.78,
    f1: 0.795,
  },
  {
    id: "naive_bayes",
    label: "Naïve Bayes",
    accuracy: 0.76,
    precision: 0.73,
    recall: 0.71,
    f1: 0.72,
  },
];

function formatMetric(value) {
  return (Math.round(value * 1000) / 1000).toLocaleString("fr-FR");
}

function renderMetricsTable(metrics) {
  const tbody = document.getElementById("metrics-body");
  tbody.innerHTML = metrics
    .map(
      (m) => `
    <tr>
      <th scope="row">${m.label}</th>
      <td>${formatMetric(m.accuracy)}</td>
      <td>${formatMetric(m.precision)}</td>
      <td>${formatMetric(m.recall)}</td>
      <td>${formatMetric(m.f1)}</td>
    </tr>`
    )
    .join("");
}

function renderComparisonBars(metrics) {
  const maxF1 = Math.max(...metrics.map((m) => m.f1), 1e-6);
  const list = document.getElementById("comparison-bars");
  list.innerHTML = metrics
    .map((m) => {
      const pct = Math.round((m.f1 / maxF1) * 100);
      return `
      <li class="bar-item">
        <span>${m.label}</span>
        <div class="bar-track" role="presentation">
          <div class="bar-fill" style="width: ${pct}%"></div>
        </div>
        <span>${formatMetric(m.f1)}</span>
      </li>`;
    })
    .join("");
}

function populateModelSelect(metrics) {
  const select = document.getElementById("model-select");
  select.innerHTML = metrics
    .map((m) => `<option value="${m.id}">${m.label}</option>`)
    .join("");
}

function handlePredictionSubmit(event) {
  event.preventDefault();
  const modelId = document.getElementById("model-select").value;
  const model = SAMPLE_METRICS.find((m) => m.id === modelId);
  const followers = Number(document.getElementById("feature-followers").value);
  const following = Number(document.getElementById("feature-following").value);

  const resultEl = document.getElementById("prediction-result");

  if (!model) {
    resultEl.textContent = "Modèle inconnu.";
    return;
  }

  /* Placeholder pédagogique : pas encore branché au backend. */
  const score =
    Number.isFinite(followers) && Number.isFinite(following)
      ? (followers + following) % 2
      : model.f1 % 1;
  const verdict =
    score > 0.45 ? "Profil probablement faux (démonstration)" : "Profil probablement authentique (démonstration)";

  resultEl.textContent = `${model.label} : ${verdict} — brancher ici la réponse JSON du serveur (Flask/FastAPI).`;
}

function init() {
  renderMetricsTable(SAMPLE_METRICS);
  renderComparisonBars(SAMPLE_METRICS);
  populateModelSelect(SAMPLE_METRICS);

  document.getElementById("predict-form").addEventListener("submit", handlePredictionSubmit);
}

document.addEventListener("DOMContentLoaded", init);
