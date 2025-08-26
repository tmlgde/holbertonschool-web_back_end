export default function getListStudentsIds(list) {
  if (!Array.isArray(list)) {
    return [];
  }
  return list.map((student) => student.id);
}
