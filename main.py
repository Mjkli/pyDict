
class Hashtable:
    # Create empty bucket
    def __init__(self,size):
        self.size = size
        self.hash_table = self.create_buckets()
    
    def create_buckets(self):
        return[[] for _ in range(self.size)]

    #Insert values into hash map
    def set_val(self, key, val):
        #Get the index from the key
        #using hash function
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_val = record

            #check if the bucket has the same key as the key to be inserted
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key,val))

    #Return value with specific key
    def get_val(self, key):
        #Get the index from the key using hash func
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_val = record
        
        #check if the bucket has the same key as the key to be inserted
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            return record_val
        else:
            return "No record"
        
    def delete_val(self,key):
        #Get the index from the key using hash func
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_val = record
        
        #check if the bucket has the same key as the key to be inserted
            if record_key == key:
                found_key = True
                break
        
        if found_key:
            bucket.pop(index)
        return


    #print Items of the hashmap
    def __str__(self) -> str:
        return "".join(str(item) for item in self.hash_table)


hash_table = Hashtable(10)

hash_table.set_val('name','def')
print(hash_table)
