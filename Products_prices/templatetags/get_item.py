import imp
from django import template
from Products_prices.models import Item


register = template.Library()


@register.filter
def get_chepest_item(supermarket, product):
            try: 
                items_list = Item.objects.filter(supermarket_branch__supermarket = supermarket, product = product) 
            except:
                return 'somthing went wrong at get_item'
            
            if len(items_list)>0:
                chepest_item = None
                temp_item = None
                for item in items_list:
                    if temp_item:
                        if item.price < temp_item.price:
                            temp_item = item
                    else:
                        temp_item = item
                           
                chepest_item = temp_item
                 
                return chepest_item.price     
                
            else:
                
                return 'N/A'



@register.filter(name = 'get_item')
def get_item(supermarket_list:list, product_list: list):    
            
            if len(supermarket_list) > 0 and len(product_list) > 0:
                
                # Iterate over all products:
                for i in range(len(product_list)):
                    
                    print(f'product: {product_list[i].name},')
                    
                    # Iterate over the supermarkets
                    for j in range(len(supermarket_list)):
                        print(f'supermarket: {supermarket_list[j].name},\n Price:')  
                        
                        # Get the chepest item with same supermarket and product.
                        item = get_chepest_item(supermarket= supermarket_list[j], product=product_list[i])
                        
                        # if the supermarket have the product
                        if item != 'N/A':
                            
                            # if item.product.name == product_list[i].name and item.supermarket_branch.supermarket.name == supermarket_list[j].name:
                                    print({item.price})
                        elif item == 'N/A':
                            print('N/A')
                        
                            
                print('__________________________________________________\n\n')
         
         
