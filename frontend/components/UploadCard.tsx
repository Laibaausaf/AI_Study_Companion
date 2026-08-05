"use client";

import { useState } from "react";
import { uploadSyllabus } from "@/lib/api";

export default function UploadCard() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [success, setSuccess] = useState(false);

  function handleFileChange(e: React.ChangeEvent<HTMLInputElement>) {
    if (e.target.files?.length) {
      setFile(e.target.files[0]);
      setSuccess(false);
    }
  }

  async function handleUpload() {
    if (!file) return;

    setUploading(true);

    try {
      await uploadSyllabus(file);
      setSuccess(true);
    } catch (error) {
      alert("Upload failed.");
      console.error(error);
    }

    setUploading(false);
  }

  return (
    <div className="bg-white rounded-2xl shadow-md p-8 max-w-3xl mx-auto">

      <h2 className="text-2xl font-semibold text-center">
        Upload Your Syllabus
      </h2>

      <p className="text-center text-gray-500 mt-2 mb-6">
        Upload your syllabus PDF to generate a personalized study plan.
      </p>

      <input
        type="file"
        accept=".pdf"
        onChange={handleFileChange}
      />

      {file && (
        <p className="mt-4 text-sm">
          Selected: <strong>{file.name}</strong>
        </p>
      )}

      <button
        onClick={handleUpload}
        disabled={!file || uploading}
        className="mt-6 w-full bg-blue-600 text-white py-3 rounded-xl hover:bg-blue-700 disabled:bg-gray-400"
      >
        {uploading ? "Uploading..." : "Upload Syllabus"}
      </button>

      {success && (
        <p className="mt-4 text-green-600 font-medium">
          ✅ Upload Successful!
        </p>
      )}

    </div>
  );
}