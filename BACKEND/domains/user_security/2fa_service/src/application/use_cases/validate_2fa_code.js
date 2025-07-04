module.exports = async (userId, code, redisClient) => {
  const storedCode = await redisClient.get(`2fa:${userId}`);
  if (!storedCode) return false;
  if (storedCode === code) {
    // Invalida el código usado
    await redisClient.del(`2fa:${userId}`);
    return true;
  }
  return false;
};
