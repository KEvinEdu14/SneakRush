class TwoFactorCode {
  constructor(userId, code, expiresAt) {
    this.userId = userId;
    this.code = code;
    this.expiresAt = expiresAt;
  }
}
module.exports = TwoFactorCode;
