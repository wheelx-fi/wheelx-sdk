/**
 * Custom error classes for WheelX SDK
 */

export class WheelXError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'WheelXError';
  }
}

export class APIError extends WheelXError {
  public statusCode: number;
  public response?: any;

  constructor(message: string, statusCode: number, response?: any) {
    super(message);
    this.name = 'APIError';
    this.statusCode = statusCode;
    this.response = response;
  }
}

export class NetworkError extends WheelXError {
  constructor(message: string) {
    super(message);
    this.name = 'NetworkError';
  }
}

export class ValidationError extends WheelXError {
  constructor(message: string) {
    super(message);
    this.name = 'ValidationError';
  }
}

export class TransactionError extends WheelXError {
  constructor(message: string) {
    super(message);
    this.name = 'TransactionError';
  }
}