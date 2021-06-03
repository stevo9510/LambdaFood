import boto3
import json

rdsData = boto3.client('rds-data')

cluster_arn = 'arn:aws:rds:us-east-1:826246783039:cluster:sanderson-aurora-project2' 
secret_arn = 'arn:aws:secretsmanager:us-east-1:826246783039:secret:dev/aurora-serverless/admin-FHZWNj' 

def formatField(field):
   return list(field.values())[0]
# Formatting query returned Field
def formatRecords(records):
   return [formatField(record[0]) for record in records]
   
def lambda_handler(event, context):
	food_parameter = event['food_name']

	foodParam = {'name':'food_name', 'value':{'stringValue': food_parameter}}
	foodParamSet = [foodParam]

	foodQuery = """
		SELECT Food.id,
			Food.food_name,
	    	Food.food_description,
	    	Food.image_url,
	    	Food.food_category_id,
	    	FoodCategory.category_name,
	    	FoodCategory.icon_path
		FROM Food
		INNER JOIN FoodCategory ON FoodCategory.id = Food.food_category_id
		WHERE Food.food_name = :food_name
		"""
	foodResponse = rdsData.execute_statement(
				resourceArn = cluster_arn, 
				secretArn = secret_arn, 
				database = 'ProjectTwoDb', 
				sql = foodQuery,
				parameters = foodParamSet)
				
	if len(foodResponse['records']) == 0:
		return { "message" : "No Results" }
	
	rec = (foodResponse['records'])[0]
	
	data = {}
	data['id'] = formatField(rec[0])
	data['food_name'] = formatField(rec[1])
	data['food_description'] = formatField(rec[2])
	data['image_url'] = formatField(rec[3])
	data['food_category_id'] = formatField(rec[4])
	data['category_name'] = formatField(rec[5])
	data['icon_path'] = formatField(rec[6])
	
	ingredientQuery = """
		SELECT FoodIngredient.ingredient_name
		FROM FoodIngredient
		WHERE food_id = :food_id
		ORDER BY FoodIngredient.sequence ASC
		"""
	
	ingredientParam = {'name':'food_id', 'value':{'longValue': data['id']}}
	ingredientParamSet = [ingredientParam]
	
	ingredientResponse = rdsData.execute_statement(
				resourceArn = cluster_arn, 
				secretArn = secret_arn, 
				database = 'ProjectTwoDb', 
				sql = ingredientQuery,
				parameters = ingredientParamSet)
	
	data['ingredients'] = formatRecords(ingredientResponse['records'])
	
	return data;