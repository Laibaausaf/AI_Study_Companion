"use client";

import { useState } from "react";
import ReactMarkdown from "react-markdown";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [days, setDays] = useState("");

  const [uploading, setUploading] = useState(false);
  const [loadingPlan, setLoadingPlan] = useState(false);

  const [message, setMessage] = useState("");
  const [studyPlan, setStudyPlan] = useState("");

  async function uploadPDF() {
    if (!file) {
      alert("Please select a PDF first.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setUploading(true);
      setMessage("");

      const response = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (response.ok) {
        setMessage("✅ PDF uploaded successfully!");
      } else {
        setMessage(data.detail || "Upload failed.");
      }
    } catch (error) {
      console.error(error);
      setMessage("❌ Could not connect to backend.");
    }

    setUploading(false);
  }

  async function generatePlan() {
  if (!days) {
    alert("Please enter the number of study days.");
    return;
  }

  try {
    setLoadingPlan(true);

    const response = await fetch(
      "http://127.0.0.1:8000/generate-study-plan",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          days: Number(days),
        }),
      }
    );

    const data = await response.json();

    if (response.ok) {
      setStudyPlan(data.study_plan);
    } else {
      alert("Failed to generate study plan.");
    }
  } catch (error) {
    console.error(error);
    alert("Could not connect to backend.");
  }

  setLoadingPlan(false);
}
  return (
    <main className="min-h-screen bg-gray-100 flex justify-center items-center p-8">

      <div className="w-full max-w-4xl bg-white rounded-2xl shadow-xl p-10">

        <h1 className="text-5xl font-bold text-center text-gray-800">
          Welcome to your AI Study Companion
        </h1>

        <p className="text-center text-gray-500 mt-4">
          Upload your syllabus and generate a personalized AI-powered study plan.
        </p>

        {/* Upload Section */}

        <div className="mt-10">

          <label className="block text-lg font-semibold mb-3">
            Upload Syllabus (PDF)
          </label>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) => {
              if (e.target.files) {
                setFile(e.target.files[0]);
              }
            }}
          />

          {file && (
            <p className="mt-3 text-green-600">
              Selected: {file.name}
            </p>
          )}

          <button
            onClick={uploadPDF}
            disabled={uploading}
            className="mt-5 bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg disabled:bg-gray-400"
          >
            {uploading ? "Uploading..." : "Upload PDF"}
          </button>

          {message && (
            <p className="mt-4 font-medium">
              {message}
            </p>
          )}

        </div>

        {/* Number of Days */}

        <div className="mt-10">

          <label className="block text-lg font-semibold mb-3">
            Complete the syllabus in
          </label>

          <input
            type="number"
            min="1"
            placeholder="e.g. 30"
            value={days}
            onChange={(e) => setDays(e.target.value)}
            className="w-full border border-gray-300 rounded-lg p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />

        </div>

        {/* Generate Button */}

        <button
          onClick={generatePlan}
          className="mt-8 w-full bg-green-600 hover:bg-green-700 text-white py-4 rounded-lg text-lg font-semibold"
        >
          Generate Study Plan
        </button>

        {/* Loading */}

        {loadingPlan && (

          <div className="mt-8 flex flex-col items-center">

            <div className="animate-spin rounded-full h-14 w-14 border-4 border-blue-600 border-t-transparent"></div>

            <p className="mt-4 text-gray-500">
              Generating your personalized study plan...
            </p>

          </div>

        )}
{/* Study Plan */}

{studyPlan && (

  <div className="mt-10 bg-white border border-gray-200 rounded-2xl shadow-lg">

    <div className="border-b px-8 py-5 flex items-center justify-between">

      <h2 className="text-3xl font-bold text-blue-700">
        📚 Your Personalized Study Plan
      </h2>

    </div>

    <div className="px-8 py-6">

      <div className="leading-8 text-gray-700 space-y-4">

        <ReactMarkdown
          components={{
            h1: ({children}) => (
              <h1 className="text-4xl font-bold text-blue-700 mb-6">
                {children}
              </h1>
            ),

            h2: ({children}) => (
              <h2 className="text-2xl font-semibold text-gray-800 mt-8 mb-4">
                {children}
              </h2>
            ),

            h3: ({children}) => (
              <h3 className="text-xl font-semibold text-gray-700 mt-6 mb-3">
                {children}
              </h3>
            ),

            p: ({children}) => (
              <p className="mb-4 leading-8">
                {children}
              </p>
            ),

            ul: ({children}) => (
              <ul className="list-disc ml-6 mb-4">
                {children}
              </ul>
            ),

            ol: ({children}) => (
              <ol className="list-decimal ml-6 mb-4">
                {children}
              </ol>
            ),

            li: ({children}) => (
              <li className="mb-2">
                {children}
              </li>
            ),

            strong: ({children}) => (
              <strong className="font-bold text-gray-900">
                {children}
              </strong>
            ),

            hr: () => (
              <hr className="my-8 border-gray-300" />
            ),

            table: ({children}) => (
              <div className="overflow-x-auto">
                <table className="table-auto border-collapse border border-gray-300 w-full my-6">
                  {children}
                </table>
              </div>
            ),

            th: ({children}) => (
              <th className="border border-gray-300 bg-gray-100 p-3 font-semibold">
                {children}
              </th>
            ),

            td: ({children}) => (
              <td className="border border-gray-300 p-3">
                {children}
              </td>
            ),
          }}
        >
          {studyPlan}
        </ReactMarkdown>

      </div>

    </div>

  </div>

)}  </div>

    </main>
  );
}