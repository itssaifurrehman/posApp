export default async function Home() {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/products", {
      cache: "no-store", // Ensures fresh data on every request
    });

    if (!res.ok) {
      throw new Error("Failed to fetch data");
    }

    const data = await res.json();

    return (
      <div>
        <h1>Products List</h1>
        {data.length > 0 ? (
          <ul>
            {data.map((item: any) => (
              <li key={item.id}>{item.name}</li>
            ))}
          </ul>
        ) : (
          <p>No products found.</p>
        )}
      </div>
    );
  } catch (error: any) {
    return <div>Error: {error.message}</div>;
  }
}
