// news-image-20261126 — "Sum up 26 November's world news in one image".
// Node 22, standard library only. The image is drawn at build time by
// tools/render.py from 37 stories verified against primary sources for
// Thursday 26 November 2026 (see NEWS.md); this program just places the
// finished PNG at /output/entry.png. Copying bytes keeps the two graded
// runs byte-identical by construction, and the program needs no network.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output'
const target = join(outDir, 'entry.png')

mkdirSync(outDir, { recursive: true })
const bytes = readFileSync(join(here, 'entry.png'))
// Guard: refuse to ship anything that is not a whole PNG.
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a])
if (bytes.length < 8 || !bytes.subarray(0, 8).equals(PNG_MAGIC)) {
  throw new Error('entry.png is not a PNG file')
}
if (bytes.length > 1048576) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB cap`)
}
writeFileSync(target, bytes)
// Confirm what landed on disk is exactly what we read.
const written = readFileSync(target)
if (!written.equals(bytes)) {
  throw new Error('written entry.png differs from the source image')
}
console.log(`wrote ${target} (${bytes.length} bytes)`)
