"use client";
import React, { useState } from "react";

const SearchBar = ({ onSearch }) => {
  const [query, setQuery] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query);
  };

  return (
    <form onSubmit={handleSubmit} className="flex w-full max-w-md mx-auto mt-4">
      <input
        type="text"
        placeholder="Search first aid tip..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="flex-grow p-2 border rounded-l-md focus:outline-none focus:ring-2 focus:ring-red-500"
      />
      <button
        type="submit"
        className="bg-red-500 text-white px-4 rounded-r-md hover:bg-red-600"
      >
        Search
      </button>
    </form>
  );
};

export default SearchBar;