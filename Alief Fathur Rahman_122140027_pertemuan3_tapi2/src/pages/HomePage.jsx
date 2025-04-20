import { Link } from "react-router-dom";
import "../styles/HomePage.css";

const HomePage = () => (
  <div className="home-container">
    <h1 className="home-title">Selamat Datang di MiniStore 🛍️</h1>
    <p className="home-subtitle">Temukan berbagai produk menarik!</p>
    <Link to="/products" className="home-button">
      Lihat Produk
    </Link>
  </div>
);

export default HomePage;
