const BASE_URL = "http://127.0.0.1:8000";

export async function uploadSyllabus(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${BASE_URL}/upload`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Upload failed");
  }

  return response.json();
}

export async function generatePlan(days: number, hours: number) {
  const question = `
Generate a detailed ${days}-day study plan.

The student can study ${hours} hour(s) per day.

Create a day-by-day schedule using only the uploaded syllabus.
`;

  const response = await fetch(`${BASE_URL}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to generate study plan");
  }

  return response.json();
}