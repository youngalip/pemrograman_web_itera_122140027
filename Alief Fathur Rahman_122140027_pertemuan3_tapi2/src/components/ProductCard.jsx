import PropTypes from 'prop-types';
import { useCart } from '../context/CartContext';
import { Link } from 'react-router-dom';
import '../styles/ProductCard.css';

const ProductCard = ({ product, onRemove, showRemoveButton = false }) => {
  const { addToCart } = useCart();

  return (
    <div className="product-card">
      <Link to={`/products/${product.id}`} className="product-link">
        <img src={product.image} alt={product.title} className="product-image" />
        <h2 className="product-title">{product.title}</h2>
        <p className="product-price">${product.price.toFixed(2)}</p>
      </Link>

      {showRemoveButton ? (
        <button className="remove-button" onClick={() => onRemove(product.id)}>
          Hapus
        </button>
      ) : (
        <button className="add-to-cart-button" onClick={() => addToCart(product)}>
          Add to Cart
        </button>
      )}
    </div>
  );
};

ProductCard.propTypes = {
  product: PropTypes.shape({
    id: PropTypes.number.isRequired,
    title: PropTypes.string.isRequired,
    image: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
  }).isRequired,
  onRemove: PropTypes.func,
  showRemoveButton: PropTypes.bool,
};

export default ProductCard;
