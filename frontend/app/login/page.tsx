"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e: any) => {
    e.preventDefault();

    // temporary login logic
    if (email && password) {
      router.push("/home");
    } else {
      alert("Please enter credentials");
    }
  };

  return (
    <div style={{
      minHeight: "100vh",
      background: "linear-gradient(135deg,#2563eb,#1e3a8a)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center"
    }}>
      <form onSubmit={handleLogin} style={{
        background: "white",
        padding: "40px",
        borderRadius: "20px",
        width: "350px",
        boxShadow: "0 20px 50px rgba(0,0,0,0.2)"
      }}>
        <h2 style={{ textAlign: "center", marginBottom: "30px" }}>
          🏥 Smart First Aid
        </h2>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e)=>setEmail(e.target.value)}
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e)=>setPassword(e.target.value)}
          style={inputStyle}
        />

        <button type="submit" style={buttonStyle}>
          LOGIN
        </button>

        <p style={{ textAlign: "center", marginTop: "15px" }}>
          Don't have an account?{" "}
          <span
            style={{ color: "#2563eb", cursor: "pointer" }}
            onClick={()=>router.push("/register")}
          >
            Register
          </span>
        </p>
      </form>
    </div>
  );
}

const inputStyle = {
  width: "100%",
  padding: "12px",
  marginBottom: "15px",
  borderRadius: "10px",
  border: "1px solid #ccc"
};

const buttonStyle = {
  width: "100%",
  padding: "12px",
  borderRadius: "10px",
  border: "none",
  background: "#ef4444",
  color: "white",
  fontWeight: "bold",
  cursor: "pointer"
};