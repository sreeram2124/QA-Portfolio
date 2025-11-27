# Test Cases for BizTrack-OMS Project

## Test Case 1: Product Search Functionality
- **Test Steps**: 
  1. Navigate to search page
  2. Enter product name "Laptop"
  3. Click search button
- **Expected**: Shows products containing "Laptop"
- **Status**: ✅ PASS

## Test Case 2: Order Creation
- **Test Steps**:
  1. Go to Orders section
  2. Click "Create New Order"
  3. Fill required fields
  4. Submit form
- **Expected**: Order appears in orders list
- **Status**: ✅ PASS

## Test Case 3: Database Connection
- **Test Steps**:
  1. Start application
  2. Check console logs
- **Expected**: "Database connected successfully"
- **Status**: ✅ PASS

## Test Case 4: User Login
- **Test Steps**:
  1. Enter valid credentials
  2. Click login
- **Expected**: Redirect to dashboard
- **Status**: ✅ PASS

## Test Case 5: Error Handling
- **Test Steps**:
  1. Enter invalid search query
  2. Submit form
- **Expected**: Show "No results found" message
- **Status**: ✅ PASS
