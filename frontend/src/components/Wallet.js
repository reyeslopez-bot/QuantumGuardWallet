import React, { useState, useEffect } from 'react';
import walletService from '../services/walletService';

const Wallet = () => {
  const [wallet, setWallet] = useState(null);

  useEffect(() => {
    walletService.createWallet().then(setWallet);
  }, []);

  return (
    <div>
      <h1>Your Wallet</h1>
      {wallet && (
        <div>
          <p>Wallet ID: {wallet.id}</p>
          <p>Balance: {wallet.balance}</p>
        </div>
      )}
    </div>
  );
};

export default Wallet;
