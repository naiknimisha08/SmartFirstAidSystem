// frontend/components/QRCodeDisplay.js
"use client";
import { QRCodeSVG } from "qrcode.react";

export default function QRCodeDisplay({ url }) {
  return <QRCodeSVG value={url} size={128} />;
}