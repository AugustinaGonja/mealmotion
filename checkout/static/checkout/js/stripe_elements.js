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
      iconColor: '#dc3545',
      color: '#dc3545',
    },
};

// Create card element & mount

const card = elements.create('card', {style});
card.mount('#card-element');



// Form Submission

form.addEventListener('submit', function (e) {
    e.preventDefault(); 

    stripe.confirmCardPayment(client_secret, {
        payment_method: {
            card: card,
            billing_details: {
                name: form.full_name?.value || "",
                email: form.email?.value || "",
            }
        }
    }).then(function (result) {

    // Handle Realtime Validation Errors

      const errorDiv = document.getElementById('card-errors');

      if (result.error) {
          errorDiv.innerHTML = `<span class="small me-2">${result.error.message}</span>`;
      } else {
          if (result.paymentIntent.status === 'succeeded') {
              form.submit();
          }
        }
    });
});