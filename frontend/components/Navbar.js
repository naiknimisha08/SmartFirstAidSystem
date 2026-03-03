export default function Navbar() {
  return (
    <nav className="bg-blue-600 text-white p-4 sticky top-0 shadow-md z-50">
      <div className="max-w-6xl mx-auto flex justify-between items-center">
        <h1 className="font-bold text-xl md:text-2xl">Smart First Aid</h1>
        <div className="space-x-6 text-sm md:text-base">
          <a href="#guidance" className="hover:underline hover:text-yellow-300">Guidance</a>
          <a href="#symptoms" className="hover:underline hover:text-yellow-300">Symptoms</a>
          <a href="#treatment" className="hover:underline hover:text-yellow-300">Treatment</a>
          <a href="#map" className="hover:underline hover:text-yellow-300">Map</a>
        </div>
      </div>
    </nav>
  );
}