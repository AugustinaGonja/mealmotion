const stripe_public_key = document.getElementById("id_stripe_public_key").textContent.slice(1, -1);
const client_secret = document.getElementById("id_client_secret").textContent.slice(1, -1);

// Initialise Stripe

const stripe = Stripe(stripe_public_key);
const elements = stripe.elements();


// Stripe CSS Styles

const style = {
    base: {
      color: '#000',
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',
      '::placeholder': {
        color: '#aab7c4',
      },
    },
    invalid: {
      iconColor: '#FFC7EE',
      color: '#FFC7EE',
    },
};

// Create card element & mount

const card = elements.create('card', {style});
card.mount('#card-element');