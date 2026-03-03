export default function Card({ title, content, type }) {
  // type: guidance / symptoms / treatment
  const colorMap = {
    guidance: "border-blue-500",
    symptoms: "border-orange-500",
    treatment: "border-green-500",
  };

  return (
    <div className={`bg-white shadow-lg rounded-lg p-6 m-4 w-72 border-l-4 ${colorMap[type]} hover:scale-105 transition-transform`}>
      <h2 className="text-xl font-bold mb-2">{title}</h2>
      <div className="text-gray-700">
        {Array.isArray(content) ? (
          <ul className="list-disc list-inside">
            {content.map((item, idx) => (
              <li key={idx}>{item}</li>
            ))}
          </ul>
        ) : (
          <p>{content}</p>
        )}
      </div>
    </div>
  );
}