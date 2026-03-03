import React from "react";

// Props: tip object and optional language ('en' or 'hi')
export default function TipDetails({ tip, language = "hi" }) {
  // Determine text to show based on language
  const conditionText = language === "hi" ? tip.condition_hi || tip.condition : tip.condition;
  const symptomsText = language === "hi" ? tip.symptoms_hi || tip.symptoms : tip.symptoms;
  const solutionText = language === "hi" ? tip.solution_hi || tip.solution : tip.solution;

  // Text-to-Speech function
  const speakTip = (text) => {
    if ("speechSynthesis" in window) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = language === "hi" ? "hi-IN" : "en-US";
      window.speechSynthesis.speak(utterance);
    } else {
      alert("Your browser does not support TTS.");
    }
  };

  return (
    <div
      style={{
        background: "white",
        padding: "30px",
        borderRadius: "20px",
        boxShadow: "0 10px 25px rgba(0,0,0,0.1)",
        maxWidth: "800px",
        margin: "40px auto",
        color: "#111827",
      }}
    >
      <h2 style={{ fontSize: "28px", fontWeight: "bold", marginBottom: "15px" }}>
        {conditionText} {tip.icon || "🚑"}
      </h2>

      {symptomsText && (
        <p style={{ marginBottom: "15px", fontSize: "16px", lineHeight: "1.5" }}>
          <strong>लक्षण / Symptoms:</strong> {symptomsText}
        </p>
      )}

      <p style={{ fontSize: "16px", lineHeight: "1.6" }}>
        <strong>उपचार / Solution:</strong> {solutionText}
      </p>

      <button
        onClick={() => speakTip(solutionText)}
        style={{
          marginTop: "20px",
          backgroundColor: "#dc2626",
          color: "white",
          border: "none",
          padding: "10px 20px",
          borderRadius: "10px",
          cursor: "pointer",
          fontWeight: "bold",
        }}
      >
        🔊 पढ़ें
      </button>
    </div>
  );
}