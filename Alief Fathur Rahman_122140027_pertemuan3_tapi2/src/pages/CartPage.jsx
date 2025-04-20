import ProductCard from "../components/ProductCard";
import { useCart } from "../context/CartContext";

const CartPage = () => {
  const { cartItems, removeFromCart } = useCart();

  const total = cartItems.reduce((acc, item) => acc + item.price, 0);

  return (
    <div className="p-4 max-w-6xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-center">Keranjang</h2>
      {cartItems.length === 0 ? (
        <p className="text-center">Keranjang kosong.</p>
      ) : (
        <>
          <div className="product-list-container">
            {cartItems.map((item) => (
              <ProductCard
                key={item.id}
                product={item}
                onRemove={removeFromCart}
                showRemoveButton
              />
            ))}
          </div>
          <div className="text-center mt-6 font-bold text-xl">
            Total: ${total.toFixed(2)}
          </div>
          <div className="text-center mt-4">
            <button className="bg-green-600 text-white px-6 py-2 rounded">
              Checkout
            </button>
          </div>
        </>
      )}
    </div>
  );
};

export default CartPage;
