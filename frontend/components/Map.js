"use client";

import { useEffect, useState } from "react";

export default function Map({ hospitals }) {
  const [LeafletMap, setLeafletMap] = useState(null);

  useEffect(() => {
    // Import only on client-side
    const loadMap = async () => {
      const { MapContainer, TileLayer, Marker, Popup } = await import(
        "react-leaflet"
      );
      const L = await import("leaflet");
      await import("leaflet/dist/leaflet.css");

      // Fix default marker icon
      delete L.Icon.Default.prototype._getIconUrl;
      L.Icon.Default.mergeOptions({
        iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
        iconUrl: require("leaflet/dist/images/marker-icon.png"),
        shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
      });

      setLeafletMap({ MapContainer, TileLayer, Marker, Popup, L });
    };

    loadMap();
  }, []);

  if (!LeafletMap) return <div>Loading map...</div>;

  const { MapContainer, TileLayer, Marker, Popup } = LeafletMap;

  return (
    <MapContainer
      center={[19.076, 72.8777]}
      zoom={13}
      style={{ height: "400px", width: "100%" }}
    >
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a>'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      {hospitals.map((h, idx) => (
        <Marker key={idx} position={[h.lat, h.lng]}>
          <Popup>{h.name}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}