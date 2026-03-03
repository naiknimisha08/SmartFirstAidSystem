"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Home() {
  const router = useRouter();
  const [language, setLanguage] = useState("hi"); // 'hi' or 'en'

  // Navigate to Injury Select page
  const startFirstAid = () => {
    router.push("/injury-select");
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "#f5f5f5",
        padding: "40px",
        color: "#111827",
        fontFamily: "'Segoe UI', sans-serif",
      }}
    >
      {/* Navbar */}
      <div
        style={{
          background: "linear-gradient(to right, #ef4444, #dc2626)",
          padding: "18px 40px",
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          color: "white",
          borderRadius: "12px",
          boxShadow: "0 8px 20px rgba(0,0,0,0.1)",
          marginBottom: "40px",
        }}
      >
        <h2 style={{ fontWeight: "bold", letterSpacing: "1px" }}>
          🚑 Smart First Aid System
        </h2>

        <div style={{ display: "flex", gap: "15px", alignItems: "center" }}>
          {/* Language Toggle */}
          <button
            onClick={() => setLanguage(language === "hi" ? "en" : "hi")}
            style={{
              padding: "8px 12px",
              borderRadius: "8px",
              border: "none",
              background: "white",
              color: "#dc2626",
              fontWeight: "bold",
              cursor: "pointer",
            }}
          >
            {language === "hi" ? "English" : "हिंदी"}
          </button>

          <button
            onClick={() => router.push("/login")}
            style={{
              padding: "10px 18px",
              borderRadius: "10px",
              border: "none",
              background: "white",
              color: "#dc2626",
              fontWeight: "bold",
              cursor: "pointer",
            }}
          >
            {language === "hi" ? "लॉग आउट" : "Logout"}
          </button>
        </div>
      </div>

      {/* Hero Section */}
      <div
        style={{
          background: "linear-gradient(135deg, #f87171, #dc2626)",
          padding: "60px 40px",
          borderRadius: "30px",
          color: "white",
          marginBottom: "40px",
          boxShadow: "0 25px 50px rgba(220,38,38,0.2)",
          textAlign: "center",
        }}
      >
        <h1 style={{ fontSize: "40px", fontWeight: "bold", marginBottom: "20px" }}>
          {language === "hi"
            ? "स्मार्ट फर्स्ट एड असिस्टेंट 🚑"
            : "Smart First Aid Assistant 🚑"}
        </h1>
        <p style={{ fontSize: "18px", maxWidth: "600px", opacity: 0.9, margin: "0 auto" }}>
          {language === "hi"
            ? "चोटों के लिए तुरंत मार्गदर्शन प्राप्त करें। तैयार रहें। तेजी से कार्य करें। जीवन बचाएँ।"
            : "Get instant emergency guidance for injuries. Stay prepared. Act fast. Save lives."}
        </p>
      </div>

      {/* Search Bar */}
      <div style={{ maxWidth: "600px", margin: "0 auto 40px auto" }}>
        <form
          onSubmit={(e) => e.preventDefault()}
          style={{ display: "flex" }}
        >
          <input
            type="text"
            placeholder={language === "hi" ? "पहला उपचार खोजें..." : "Search first aid tip..."}
            style={{
              flexGrow: 1,
              padding: "10px",
              borderRadius: "8px 0 0 8px",
              border: "1px solid #ccc",
              outline: "none",
            }}
          />
          <button
            type="submit"
            style={{
              padding: "10px 20px",
              borderRadius: "0 8px 8px 0",
              border: "none",
              backgroundColor: "#dc2626",
              color: "white",
              cursor: "pointer",
            }}
          >
            {language === "hi" ? "खोजें" : "Search"}
          </button>
        </form>
      </div>

      {/* Start First Aid Button */}
      <div style={{ textAlign: "center", marginTop: "40px" }}>
        <button
          onClick={startFirstAid}
          style={{
            padding: "15px 30px",
            fontSize: "18px",
            fontWeight: "bold",
            color: "#dc2626",
            backgroundColor: "white",
            borderRadius: "12px",
            cursor: "pointer",
            boxShadow: "0 10px 25px rgba(0,0,0,0.15)",
            transition: "0.3s",
          }}
          onMouseOver={(e) => (e.currentTarget.style.transform = "scale(1.05)")}
          onMouseOut={(e) => (e.currentTarget.style.transform = "scale(1)")}
        >
          {language === "hi" ? "प्रथम चिकित्सा शुरू करें" : "Start First Aid"}
        </button>
      </div>
    </div>
  );
}