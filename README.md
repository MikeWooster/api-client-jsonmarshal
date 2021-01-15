# Python API Client Json Marshal Extension

## Installation

```
pip install api-client-jsonmarshal
```

## Usage

The following decorators have been provided to marshal request data as python dataclasses to json
and to unmarshal json directly into a python dataclass.

```
# Marshal dataclass -> json
@marshal_request(date_fmt: Optional[str] = None, datetime_fmt: Optional[str] = None)

# Unmarshal json -> dataclass
@unmarshal_response(schema: T, date_fmt: Optional[str] = None, datetime_fmt: Optional[str] = None)
```

Usage:
1. Define the schema for your api in python dataclasses.
2. Add the `@unmarshal_response` decorator to the api client method to transform the response
directly into your defined schema.
   ```
   @unmarshal_response(List[Account])
   def get_accounts():
       ...
   ```
3. Add the `@marshal_request` decorator to the api client method to translate the incoming dataclass
into the required json for the endpoint:
   ```
   @marshal_request()
   def create_account(account: Account):
      ...
   ```

The marshalling functionality has been provided by: https://github.com/MikeWooster/jsonmarshal
More usage examples can be found there.
