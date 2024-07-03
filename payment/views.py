import razorpay
from rest_framework import generics, status
from rest_framework.response import Response


class CreateOrder(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        client = razorpay.Client(auth=("rzp_test_sWtqzDmEdXb6EG", "BpDLBFiT9zu3ogC5wHLBAK9J"))
        client.set_app_details({"title": "CMS", "version": "1.00"})
        order_resp = client.order.create({
            "amount": 50000,
            "currency": "INR",
            "receipt": "receipt#1",
            "partial_payment": False,
            "notes": {
                "key1": "value3",
                "key2": "value2"
            }
        })
        print("Gateway - Create Order Resp [%s]", order_resp)

        if 'error' in order_resp or 'id' not in order_resp:
            return Response(data=order_resp, status=status.HTTP_502_BAD_GATEWAY)

        return Response(data=order_resp, status=status.HTTP_201_CREATED)

