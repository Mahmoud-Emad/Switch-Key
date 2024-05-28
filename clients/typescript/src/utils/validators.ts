/**
 * Validates if a given string is a valid UUID format.
 *
 * @param {string} uuid - The string to be validated as a UUID.
 * @returns {boolean} - Returns true if the string is a valid UUID format, otherwise false.
 */
export function UUIDValidators(uuid: string): boolean {
  const uuidRegex =
    /^[0-9a-f]{8}-[0-9a-f]{4}-[4][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
  return uuidRegex.test(uuid);
}
