import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker()


def generate_mock_orders(num_orders = 1000):
    orders = []
    
    base_time = datetime.now()
    
    for _ in range(num_orders):
        order_time = base_time - timedelta(minutes=random.randint(10,300))
        
        delivery_time = order_time + timedelta(minutes=random.randint(15,60))
        
        order = {
            "order_id": fake.uuid4(),
            "customer_id":fake.uuid4()[:8],
            "restaurant_id":random.choice(["REST_A","REST_B","REST_C","REST_D"]),
            "order_timestamp": order_time.strftime("%Y-%m-%d %H:%M:%S"),
            "delivery_timestamp": delivery_time.strftime("%Y-%m-%d %H:%M:%S"),
            "order_value_eur": round(random.uniform(10.0,75.0), 2),
            "city": "Amsterdam"
        }
        
        orders.append(order)
        
    return pd.DataFrame(orders)

if __name__ == "__main__":
    print("Generating Mock JustEatTakeAway orders Please take your seats....")
    
    df_orders = generate_mock_orders(100)
    
    file_name = "raw_orders.csv"
    df_orders.to_csv(file_name,index=False)
    
    print(f'Successfully generated 100 orders and saved to {file_name}')