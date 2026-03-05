// frontend/utils/api.js
export const BASE_URL = "http://127.0.0.1:8000"; // correct colon

export async function fetchGuidance() {
  try {
    const res = await fetch(`${BASE_URL}/guidance`);
    return await res.json();
  } catch (err) {
    console.error("Failed to fetch guidance:", err);
    return null;
  }
}

export async function fetchSymptoms() {
  try {
    const res = await fetch(`${BASE_URL}/symptoms`);
    return await res.json();
  } catch (err) {
    console.error("Failed to fetch symptoms:", err);
    return null;
  }
}

export async function fetchTreatment() {
  try {
    const res = await fetch(`${BASE_URL}/treatment`);
    return await res.json();
  } catch (err) {
    console.error("Failed to fetch treatment:", err);
    return null;
  }
}