class Notification {
  constructor(to, message) {
    this.to = to;
    this.message = message;
    this.status = 'queued';
    this.created_at = new Date();
  }
}
module.exports = Notification;
