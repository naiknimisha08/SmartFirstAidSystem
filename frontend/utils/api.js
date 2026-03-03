const BASE_URL = "http://127.0.0.1:8000/firstaid"; // Replace with your backend URL if deployed

export async function fetchGuidance() {
  const res = await fetch(`${BASE_URL}/guidance`);
  return res.json();
}

export async function fetchSymptoms() {
  const res = await fetch(`${BASE_URL}/symptoms`);
  return res.json();
}

export async function fetchTreatment() {
  const res = await fetch(`${BASE_URL}/treatment`);
  return res.json();
}