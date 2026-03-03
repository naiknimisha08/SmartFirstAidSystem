"use client";

import { QRCodeSVG } from "qrcode.react";

export default function QRCodeDisplay({ url }) {
  return (
    <div className="mt-16 p-8 text-center bg-white shadow-lg rounded-lg max-w-md mx-auto">
      <h2 className="text-2xl font-semibold mb-4">Scan to Open Online</h2>
      <QRCodeSVG value={url} size={200} />
      <p className="mt-4 text-gray-600 break-words">{url}</p>
    </div>
  );
}